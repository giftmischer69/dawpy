from cmd import Cmd
from pathlib import Path
from tkinter import filedialog

from dawpy._version import __version__
from dawpy.core.daw import Daw, VstPlugin
import os
import os.path


# https://github.com/yaronn/wopr
# https://github.com/willmcgugan/rich

# make dawpy like vim !!!!!!! modes / cmds / go into pattern etc.

# https://docs.python.org/3/library/curses.panel.html

class View:
    @classmethod
    def print_daw(cls, daw):
        print(daw.__dict__)


class Shell(Cmd):
    """ the dawpy shell, based on the built in python cmd module
    commands are based on the "mkdir" naming convention:
    - mk -> make
    - pr -> print
    - cr -> create

    - pat -> pattern
    - plug -> plugin

    etc...
    """

    def __init__(self):
        super().__init__()
        self.prompt = "dsh>"
        self.daw = Daw()
        self.view = View()
        self.debug = True

    def preloop(self):
        print(f"welcome to the dawpy shell, version: {__version__}")
        self.do_help("")

    def do_q(self, line):
        """ Quits the shell """
        return True

    def do_prdaw(self, line):
        """ Prints the daw """
        self.view.print_daw(self.daw)

    def do_crpat(self, line):
        """ create pattern """
        name = self.ask_string("enter pattern name")
        bpm = self.daw.project.bpm
        midi_file = self.ask_file_indexed("choose midi file", None, ".mid")

        dll = self.ask_file_indexed("choose plugin dll", None, ".dll")
        fxp = self.ask_file_indexed("choose plugin fxp", None, ".fxp")
        is_32bit = self.ask_bool("is this plugin 32bit?")

        p = VstPlugin(dll, fxp, is_32bit)

        bar_offset = self.ask_int("enter bar offset")

        self.daw.create_midi_pattern(name, bpm, midi_file, p, bar_offset)

    def do_rd(self, line):
        """ render current project
        Usage: rd [out_file]
        """
        if not line or not line.strip():
            print("ERROR! Usage: rd [out_file]")
        else:
            self.daw.render(line)



    def ask_file_indexed(self, dialog: str, initial_dir, expected_suffix: str):
        if not initial_dir:
            initial_dir = os.getcwd()

        # https://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
        print(dialog)
        files = []
        for dir_path, dir_names, filenames in os.walk(initial_dir):
            for filename in [f for f in filenames if f.endswith(expected_suffix)]:
                path = Path(os.path.join(dir_path, filename)).absolute()
                files.append(path)

        for i, x in enumerate(files):
            name = x.name.replace(x.suffix, "")
            print(f"{i}:\t {name}")

        choice = self.ask_int("choose one file")
        return files[choice]

    def ask_string(self, dialog: str):
        return input(f"{dialog}\n: ")

    def ask_int(self, dialog: str):
        return int(input(f"{dialog}\n: "))

    def ask_bool(self, dialog: str):
        return "y" in input(f"{dialog} (Y/n)\n: ").lower()
