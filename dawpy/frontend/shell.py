from cmd import Cmd
from pathlib import Path
from tkinter import filedialog

from dawpy._version import __version__
from dawpy.core.daw import Daw, VstPlugin, MidiTypes, Project
import os
import os.path
import yaml


# https://github.com/yaronn/wopr
# https://github.com/willmcgugan/rich

# make dawpy like vim !!!!!!! modes / cmds / go into pattern etc.

# https://docs.python.org/3/library/curses.panel.html

class View:
    @classmethod
    def print_daw(cls, daw):
        print(yaml.dump(daw))


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

        if self.ask_bool("generate midi file?"):
            type = self.ask_indexed("choose midi type", MidiTypes.enum_members)
            midi_file = self.daw.generate_midi_file(type)
        else:
            midi_file = self.ask_file_indexed("choose midi file", None, ".mid")

        dll = self.ask_file_indexed("choose plugin dll", None, ".dll")
        fxp = self.ask_file_indexed("choose plugin fxp", None, ".fxp")
        is_32bit = self.ask_bool("is this plugin 32bit?")

        p = VstPlugin(dll, fxp, is_32bit)

        bar_offset = self.ask_int("enter bar offset")

        self.daw.create_pattern(name, bpm, midi_file, p, bar_offset)

    def do_rd(self, line):
        """ render current project
        Usage: rd [out_file]
        """
        if not line or not line.strip():
            print("ERROR! Usage: rd [out_file]")
        else:
            self.daw.render(line)

    def do_sv(self, line):
        """ save current project """
        self.daw.save_project()

    def do_ld(self, line):
        """ load project
        Usage: ld or ld [project_name]
        """
        if not line or not line.strip():
            path = self.ask_file_indexed("choose project", None, ".yaml")
            project_name = path.name.replace(".yaml", "")
            print(f"project_name: {project_name}")
            self.daw.load_project(project_name)
        else:
            self.daw.load_project(line)

    def do_sq(self, line):
        """ save, then quit """
        self.do_svproj(line)
        self.do_q(line)

    def do_np(self, line):
        """ create new project
        Usage: np or np [name_no_spaces] [bpm] [key]"""
        if not line or not line.strip():
            project_name = self.ask_string("enter project name")
            project_bpm = self.ask_string("enter project bpm")
            project_key = self.ask_string("enter project key")
        else:
            args = line.split(" ")
            print(args)
            project_name = args[0]
            project_bpm = args[1]
            project_key = args[2]

        self.daw.project = Project(project_name, project_bpm, project_key)

    def ask_file_indexed(self, dialog: str, initial_dir, expected_suffix: str):
        if not initial_dir:
            initial_dir = os.getcwd()

        # https://stackoverflow.com/questions/954504/how-to-get-files-in-a-directory-including-all-subdirectories
        print(dialog)
        files = []
        for dir_path, dir_names, filenames in os.walk(initial_dir):
            for filename in [f for f in filenames if f.lower().endswith(expected_suffix.lower())]:
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

    def ask_indexed(self, dialog, enum_members):
        print(dialog)
        for i, v in enum_members:
            print(f"{i}:\t {v}")
        choice = self.ask_int("choose one file")
        return enum_members[choice]
