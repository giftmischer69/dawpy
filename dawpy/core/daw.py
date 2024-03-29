import logging
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

import yaml
from melodia.core import Track, Tone, Note
from melodia.music import chord
from melodia.io import midi


def run_checked(command):
    proc = subprocess.run(
        command,
        stdout=sys.stdout,
        shell=True,
    )
    return_code = proc.returncode
    logging.info(f"return_code: {return_code}")
    if return_code != 0:
        raise Exception


class MidiProducer:
    @classmethod
    def produce_midi(cls, key: str = "C") -> Path:
        ...


class SnareMidiProducer(MidiProducer):
    @classmethod
    def produce_midi(cls, key: str = "C") -> Path:
        logging.info("generating snare midi")
        track = Track(signature=(4, 4))
        tone = Tone.from_notation("C5")  # c4, d3

        note_q_rest = Note(tone, (1, 4), 0)
        note_q_hit = Note(tone, (1, 4), 1)

        track.add(note_q_rest)
        track.add(note_q_hit)
        track.add(note_q_rest)
        track.add(note_q_hit)

        Path("./data/generated/").mkdir(parents=True, exist_ok=True)
        p = Path("./data/generated/snare.mid").absolute()
        with open(p, "wb") as f:
            midi.dump(track, f)
        return p


class KickMidiProducer(MidiProducer):
    ...


class ChordMidiProducer(MidiProducer):
    ...


class BassMidiProducer(MidiProducer):
    ...


class VstPlugin:
    def __init__(
        self,
        name: str,
        dll: Path,
        is_32bit: bool,
        preset_folder: Path,
        selected_fxp: Path,
    ):
        self.name = name
        self.dll = dll
        self.is_32bit = is_32bit
        self.preset_folder = preset_folder
        self.selected_fxp = selected_fxp


class VstPluginRenderer:
    mrs_watson_32 = Path(
        "./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson.exe"
    ).absolute()
    mrs_watson_64 = Path(
        "./plugins/tools/MrsWatson-0.9.8/Windows/mrswatson64.exe"
    ).absolute()

    @classmethod
    def render(cls, vstplugin, midi_file, out_file):
        ...


class Pattern:
    def __init__(
        self, name: str, bpm: float, key: str, plugin: VstPlugin, midi_file: Path
    ):
        self.name = name
        self.bpm = bpm
        self.key = key
        self.plugin = plugin
        self.midi_file = midi_file


class Project:
    def __init__(self, name: str = "default", bpm: float = 90, key: str = "C"):
        self.name = name
        self.bpm = bpm
        self.key = key
        self.playlist: List[Tuple[int, Pattern]] = []
        self.registered_plugins: List[VstPlugin] = []

    def add_midi_pattern(self, entry: Tuple[int, Pattern]):
        self.playlist.append(entry)


class Daw:
    def __init__(
        self,
        user_name: str = "anon",
        project_name: str = "default",
        project_bpm: int = 90,
        project_key: str = "C",
    ):
        self.user_name = user_name
        self.project: Project = Project(project_name, project_bpm, project_key)

    def render(self, out_file: Path):
        """ renders to file """
        # - for each pattern render wit VstPluginRenderer
        # - then prepend  with offset silence
        # - then render to temp file
        # - then merge temp files
        print(yaml.dump(self.project))
        for offset, pattern in self.project.playlist:
            p = Path(f"./data/generated/{pattern.name}.wav")
            if pattern.plugin.is_32bit:
                command = f'"{VstPluginRenderer.mrs_watson_32}"'
            else:
                command = f'"{VstPluginRenderer.mrs_watson_64}"'

            command += f' --midi-file "{pattern.midi_file.absolute()}" --output "{p}" --plugin "{pattern.plugin.dll.absolute()}","{pattern.plugin.selected_fxp.absolute()}"'

            print("running command: " + command)

            run_checked(command)


    def create_pattern(
        self,
        name: str,
        bpm: float,
        key: str,
        midi_file: Path,
        plugin: VstPlugin,
        bar_offset: int,
    ):
        pattern = Pattern(name, bpm, key, plugin, midi_file)
        self.project.add_midi_pattern((bar_offset, pattern))

    def delete_pattern(self, index: int):
        del self.project.playlist[index]

    def save_project(self):
        Path("./data/projects/").mkdir(parents=True, exist_ok=True)
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
