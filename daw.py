from tkinter import filedialog

import os

import typer
from jinja2 import Template
from pathlib import Path

from models import Daw, Pattern, Playlist, Plugin
from cmd import Cmd
import json
from selenium import webdriver
import py_midicsv as pm


# import platform


class View:
    def print_daw(self, daw):
        parsed = json.loads(daw.json())
        print(json.dumps(parsed, indent=4, sort_keys=True))

    def write_html(self, daw, view_file_name):
        with open("view/template.html", "r") as f:
            template = Template(f.read())
        with open("view/layout.css", "r") as f:
            layout = f.read()
        daw_config = str(daw.daw_config)
        ret = template.render(
            layout=layout,
            daw_config=daw_config
        )
        with open(view_file_name, "w") as f:
            f.write(ret)


class Prompt(Cmd):
    # TODO: IMPLEMENT ONLY THIS! BUT RIGHT THIS TIME! THEN SERVER THEN ANGULAR FRONT
    # Project: dawpy suite / dsuite
    # Has: dawpy tools dtool / dawpy shell dshell dawpysh /
    # THIS: dshell / dserver / d

    # handles cmd line interaction with the user and calls other api
    # has a view object
    # has a daw object
    def __init__(self, headless):
        super().__init__()
        self.prompt = "dsh>"
        self.daw = Daw()
        self.view = View()
        self.headless = headless
        if not self.headless:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.browser = webdriver.Chrome(options=options)
            self.view_file_name = "view.html"
            self.view.write_html(self.daw, self.view_file_name)
            self.view_url = f"file:///{Path(self.view_file_name).absolute()}"
            self.browser.get(self.view_url)

    def ask_file(self, dialoge: str, initialdir=None):
        print(dialoge)
        if not initialdir:
            initialdir = os.getcwd()
        return filedialog.askopenfilename(title=dialoge, initialdir=initialdir)

    def ask_folder(self, dialoge: str, initialdir=None):
        print(dialoge)
        if not initialdir:
            initialdir = os.getcwd()
        return filedialog.askdirectory(title=dialoge, initialdir=initialdir)

    def ask_string(self, dialog: str):
        return input(f"{dialog}\n: ")

    def ask_int(self, dialog: str):
        return int(input(f"{dialog}\n: "))

    def do_q(self, line):
        """ Quits the shell """
        return True

    def do_pd(self, line):
        """ Prints the daw """
        self.view.print_daw(self.daw)

    def do_rp(self, line):
        """ Register Plugin. \n\t Usage: rp [plugin_name] """
        args = str(line).split(" ")[1:]
        if len(args) == 0:
            name = self.ask_string("enter plugin name")
        elif len(args) == 1:
            name = args[0]
        else:
            name = args[0]
            print(f"i'll take this name {name} but i got too many arguments")
        dll_path = self.ask_file("enter plugin dll path", self.daw.daw_config.plugin_path)
        preset_path = self.ask_file("enter plugin fxp patch path", self.daw.daw_config.preset_path)
        p = Plugin(name, dll_path, preset_path)
        self.daw.register_plugin(p)

    def do_midicsv(self, line):
        """ Convert midi to csv \n\t Usage: midicsv [midi_path] [output_file] """
        args = str(line).split(" ")[1:]
        if len(args) == 0:
            midi_file = self.ask_file("enter midi path")
            out_file = self.ask_string("enter output file name")
        elif len(args) == 1:
            midi_file = args[0]
            out_file = self.ask_string("enter output file name")
        elif len(args) == 2:
            midi_file = args[0]
            out_file = args[1]
        else:
            midi_file = args[0]
            out_file = args[1]
            print(f"i'll take this midi file {midi_file} and this out file {out_file} but i got too many arguments")
        # Load the MIDI file and parse it into CSV format
        csv_list: list = pm.midi_to_csv(midi_file)
        csv_string = " ".join(csv_list)
        print(csv_string)
        with open(f"{out_file}.csv", "w") as f:
            f.write(csv_string)

    def postcmd(self, stop, line):
        print(f"postcmd stop:{stop}")
        if not self.headless:
            self.view.write_html(self.daw, self.view_file_name)
            self.browser.refresh()
        if stop:
            print("goodbye")
            exit()


app = typer.Typer()


@app.callback(invoke_without_command=True)
@app.command()
def shell(headless: bool = True):
    p = Prompt(headless=headless)
    p.cmdloop()
    print("shut down correctly")


if __name__ == '__main__':
    app()
