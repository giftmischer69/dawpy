import logging

import subprocess
import sys
from enum import Enum
from pathlib import Path
from typing import List, Tuple
import sox
import tempfile

import pickle
import yaml

"""
# daw.py - core functionality of dawpy

a pattern has a render function that returns a sox array or sth
todo define abstract classes for different pattern types
 
"""


# genos.se - shaping the future for fun
#            empowering artists for fun
#            contributing to society for fun


def run_checked(command):
    proc = subprocess.run(command, stdout=sys.stdout, shell=True, )
    return_code = proc.returncode
    logging.info(f"return_code: {return_code}")
    if return_code != 0:
        raise Exception


class VstPlugin:
    def get_plugin_name(self) -> str:
        return self.dll.name.replace(self.dll.suffix, "")

    def get_preset_name(self) -> str:
        return self.fxp.name.replace(self.fxp.suffix, "")

    def __init__(self, dll: Path, fxp: Path, is_32bit: bool):
        self.dll: Path = dll
        self.fxp: Path = fxp
        self.is_32bit: bool = is_32bit


class Pattern:
    """ ## MidiPattern
    a MidiPattern can render a bar from a
    - midi file & plugin
    """

    def __init__(self, name: str, bpm: int, midi_file: Path, plugin: VstPlugin):
        self.name = name
        self.bpm = bpm
        self.midi_file = midi_file  # TODO dynamically create midi file with tempo
        self.plugin = plugin


class MidiTypes(Enum):
    CHORD = 0
    BASS = 1
    SNARE = 2
    KICK = 3
    HI_HAT = 4


class Project:
    def __init__(self, name, bpm, key):
        self.name = name
        self.bpm = bpm
        self.key = key
        self.playlist: List[Tuple[int, Pattern]] = []

    def add_midi_pattern(self, entry: Tuple[int, Pattern]):
        self.playlist.append(entry)


class Daw:
    # TODO pickle -> yaml
    # TODO midi generation (mingus)

    mrs_watson_32 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson.exe").absolute()
    mrs_watson_64 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson64.exe").absolute()
    nano_host_32 = Path("./plugins/tools/Tone2 NanoHost v1.0.2/NanoHost32bit.exe").absolute()
    nano_host_64 = Path("./plugins/tools/Tone2 NanoHost v1.0.2/NanoHost64bit.exe").absolute()

    # NOTE: RustPython -> WebAssembly -> Web based :)
    def __init__(self, user_name: str = "anon", project_name: str = "default", project_bpm: int = 90,
                 project_key: str = "C"):
        self.user_name = user_name
        self.project: Project = Project(project_name, project_bpm, project_key)

    def create_pattern(self, name: str, bpm: int, midi_file: Path, plugin: VstPlugin, bar_offset: int):
        # choose/configure instrument, choose/configure midi for pattern
        # render patterns, render together

        pattern = Pattern(name, bpm, midi_file, plugin)
        self.project.add_midi_pattern((bar_offset, pattern))

    def configure_plugin(self, plugin) -> None:
        if plugin.is_32bit:
            run_checked(f"\"{self.nano_host_32}\" \"{plugin.dll}\"")
        else:
            run_checked(f"{self.nano_host_64} {plugin.dll}")

    def save_project(self):
        path = Path(f"./data/projects/{self.project.name}.yaml").absolute()
        with open(path, "w") as p:
            yaml.dump(self.project, p, Dumper=yaml.Dumper)

    def load_project(self, project_name):
        path = Path(f"./data/projects/{project_name}.yaml").absolute()
        with open(path, "r") as p:
            self.project = yaml.load(p, Loader=yaml.Loader)

    def save_project_pickle(self):
        path = Path(f"./data/projects/{self.project.name}.pkl").absolute()
        with open(path, 'wb') as p:
            pickle.dump(self.project, p)

    def load_project_pickle(self, project_name):
        path = Path(f"./data/projects/{project_name}.pkl").absolute()
        with open(path, 'rb') as p:
            self.project = pickle.load(p)

    def render(self, out_file):
        rendered_arrays = []
        rendered_files = []
        for offset, pattern in self.project.playlist:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
                out = Path(temp.name).absolute()
                if pattern.plugin.is_32bit:
                    command = f"\"{self.mrs_watson_32}\""
                else:
                    command = f"\"{self.mrs_watson_64}\""

                command += f" --midi-file \"{pattern.midi_file.absolute()}\" --output \"{out}\" --plugin \"{pattern.plugin.dll.absolute()}\",\"{pattern.plugin.fxp.absolute()}\""
                print("running command: " + command)
                run_checked(command)
                tfm = sox.Transformer()
                # 60,000 (ms) ÷ BPM = duration of a quarter note
                offset_ms = (60000 / self.project.bpm) * offset
                tfm.pad(start_duration=offset_ms)

                arr = tfm.build_array(out.__str__())
                print(f"result: {len(arr)}")
                rendered_arrays.append(arr)

        logging.warning(len(rendered_arrays))
        logging.warning(len(rendered_files))

        tfm = sox.Transformer()
        for a in rendered_arrays:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
                path = Path(temp.name).absolute()
                logging.warning(path)
                tfm.build(None, path.__str__(), a, sample_rate_in=44100)
                rendered_files.append(path.__str__())

        cbn = sox.Combiner()
        cbn.build(rendered_files, out_file, "mix")
