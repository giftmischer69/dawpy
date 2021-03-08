import logging

import subprocess
import sys
from pathlib import Path
from typing import Any, List, Tuple

import tempfile
import sox
from abc import ABC, abstractmethod
import numpy as np
import tempfile

"""
# daw.py - core functionality of dawpy

a pattern has a render function that returns a sox array or sth
todo define abstract classes for different pattern types
 
"""


# genos.se - shaping the future for fun
#            empowering artists for fun
#            contributing to society for fun


class Pattern(ABC):
    def __init__(self, name: str = "pattern", bpm: int = 90):
        self.name = name
        self.bpm = bpm

    @abstractmethod
    def render(self) -> np.ndarray:
        """ a pattern can render itself, returns the rendered pattern as binary sound data in a numpy ndarray """
        ...


class WavPattern(Pattern, ABC):
    def __init__(
            self,
            name: str = "pattern",
            bpm: int = 90,
            wav_file: Path = None,
            wav_bars: int = 4,
    ):
        super().__init__(name, bpm)
        self.wav_file = wav_file
        self.wav_bars = wav_bars


def run_checked(command):
    proc = subprocess.run(command, stdout=sys.stdout, shell=True, )
    return_code = proc.returncode
    logging.info(f"return_code: {return_code}")
    if return_code != 0:
        raise Exception


class VstPlugin:
    mrs_watson_32 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson.exe").absolute()
    mrs_watson_64 = Path("./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson64.exe").absolute()
    nano_host_32 = Path("./plugins/tools/Tone2 NanoHost v1.0.2/NanoHost32bit.exe").absolute()
    nano_host_64 = Path("./plugins/tools/Tone2 NanoHost v1.0.2/NanoHost64bit.exe").absolute()

    def configure(self) -> None:
        if self.is_32bit:
            run_checked(f"\"{self.nano_host_32}\" \"{self.dll}\"")
        else:
            run_checked(f"{self.nano_host_64} {self.dll}")

    def get_plugin_name(self) -> str:
        return self.dll.name.replace(self.dll.suffix, "")

    def get_preset_name(self) -> str:
        return self.fxp.name.replace(self.fxp.suffix, "")

    def __init__(self, dll: Path, fxp: Path, is_32bit: bool):
        self.dll: Path = dll
        self.fxp: Path = fxp
        self.is_32bit: bool = is_32bit

    def render(self, midi: Path) -> np.ndarray:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
            out = Path(temp.name).absolute()
            if self.is_32bit:
                command = f"\"{self.mrs_watson_32}\""
            else:
                command = f"\"{self.mrs_watson_64}\""

            command += f" --midi-file \"{midi.absolute()}\" --output \"{out}\" --plugin \"{self.dll.absolute()}\",\"{self.fxp.absolute()}\""
            print("running command: " + command)
            run_checked(command)
            # temp.write('Some data')

            tfm = sox.Transformer()
            arr = tfm.build_array(out.__str__())
            print(f"result: {len(arr)}")
            return arr


class MidiPattern(Pattern, ABC):
    """ ## MidiPattern
    a MidiPattern can render a bar from a
    - midi file & plugin
    """

    def __init__(self, name: str, bpm: int, midi_file: Path, plugin: VstPlugin):
        super().__init__(name, bpm)
        self.midi_file = midi_file  # TODO dynamically create midi file with tempo
        self.plugin = plugin

    def render(self) -> np.ndarray: #TODO: rething rendering chain
        return self.plugin.render(self.midi_file)


class Project:
    def __init__(self, name, bpm):
        self.name = name
        self.bpm = bpm
        self.playlist: List[Tuple[int, Pattern]] = []

    def add_midi_pattern(self, entry: Tuple[int, Pattern]):
        self.playlist.append(entry)

    def render(self, out_file):
        for offset, pattern in self.playlist:
            rendered = pattern.render(out_file)
            # todo bpm to bar length
            offset_ms = 0 # bpm / 90 oder so
            tfm = sox.Transformer()
            tfm.pad(start_duration=offset_ms)
            tfm.build(None, out_file, rendered)




class Daw:

    def __init__(self, user_name: str = "anon", project_name: str = "default", project_bpm: int = 90):
        self.user_name = user_name
        self.project: Project = Project(project_name, project_bpm)

    def create_midi_pattern(self, name: str, bpm: int, midi_file: Path, plugin: VstPlugin, bar_offset: int):
        # choose/configure instrument, choose/configure midi for pattern
        # render patterns, render together

        pattern = MidiPattern(name, bpm, midi_file, plugin)
        self.project.add_midi_pattern((bar_offset, pattern))

    def render(self, out_file):
        self.project.render(out_file)
