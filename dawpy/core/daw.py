import logging
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

import yaml


def run_checked(command):
    proc = subprocess.run(command, stdout=sys.stdout, shell=True, )
    return_code = proc.returncode
    logging.info(f"return_code: {return_code}")
    if return_code != 0:
        raise Exception


class MidiProducer:
    @classmethod
    def generate_midi(cls, key: str = "C") -> Path:
        ...


class SnareMidiProducer(MidiProducer):
    ...


class KickMidiProducer(MidiProducer):
    ...


class ChordMidiProducer(MidiProducer):
    ...


class BassMidiProducer(MidiProducer):
    ...


class VstPlugin:
    def __init__(self, name: str, dll: Path, is_32bit: bool, preset_folder: Path, selected_fxp: Path):
        self.name = name
        self.dll = dll
        self.is_32bit = is_32bit
        self.preset_folder = preset_folder
        self.selected_fxp = selected_fxp


class VstPluginRenderer:
    mrs_watson_32 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson.exe").absolute()
    mrs_watson_64 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson64.exe").absolute()

    @classmethod
    def render(cls, vstplugin, midi_file, out_file):
        ...


class Pattern:
    def __init__(self, name: str, bpm: float, key: str, plugin: VstPlugin, midi_file: Path = None):
        self.name = name
        self.bpm = bpm
        self.key = key
        self.plugin = plugin
        if not midi_file:
            midi_file = MidiProducer.generate_midi(key)
        self.midi_file = midi_file


class Project:
    def __init__(self, name: str = "default", bpm: float = 90, key: str = "C"):
        self.name = name
        self.bpm = bpm
        self.key = key
        self.playlist: List[Tuple[int, Pattern]] = []

    def add_midi_pattern(self, entry: Tuple[int, Pattern]):
        self.playlist.append(entry)


class Daw:
    def __init__(self, user_name: str = "anon", project_name: str = "default", project_bpm: int = 90,
                 project_key: str = "C"):
        self.user_name = user_name
        self.project: Project = Project(project_name, project_bpm, project_key)

    def render(self, out_file: Path):
        """ renders to file """
        # - for each pattern render wit VstPluginRenderer
        # - then prepend  with offset silence
        # - then render to temp file
        # - then merge temp files
        ...

    def create_pattern(self, name: str, bpm: int, midi_file: Path, plugin: VstPlugin, bar_offset: int):
        pattern = Pattern(name, bpm, midi_file, plugin)
        self.project.add_midi_pattern((bar_offset, pattern))

    def delete_pattern(self, index: int):
        del self.project.playlist[index]

    def save_project(self):
        path = Path(f"./data/projects/{self.project.name}.yaml").absolute()
        with open(path, "w") as p:
            yaml.dump(self.project, p, Dumper=yaml.Dumper)

    def load_project(self, project_name):
        path = Path(f"./data/projects/{project_name}.yaml").absolute()
        with open(path, "r") as p:
            self.project = yaml.load(p, Loader=yaml.Loader)


class TempFileManager:
    def getTempFile(self):
        ...

    def getTempFolder(self):
        ...

    def cleanTempFolder(self):
        ...
