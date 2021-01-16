import os
import re
from tkinter import filedialog

import requests
import typer

from daw import Daw


class Command:
    def __init__(self, command_string: str, description: str, func):
        self.command_string = command_string
        self.description = description
        self.func = func

    def list_commands_func(self) -> int:
        print(f"cmd: {self.command_string} todo: list_commands_func")
        return 0

    def __call__(self, *args, **kwargs) -> int:
        """ :param """
        if len(args) != 0:
            options = args[0]
        elif len(kwargs) != 0:
            options = kwargs["options"]
        else:
            options = []
        options = options[0]
        Prompt.dbg_print(f"{self.command_string} __call__ {args} -> {options}")
        if len(options) == 0:
            return self.func()
        else:
            return self.func(options)


class Prompt:
    debug = False

    @classmethod
    def dbg_print(cls, string: str):
        if cls.debug:
            print(string)

    def __init__(self, debug: bool = False):
        Prompt.debug = debug
        self.daw: Daw = None
        self.running = True
        self.commands = [
            Command("q", "exit the shell", self.exit_func),
            Command("exit", "exit the shell", self.exit_func),
            Command("lc", "list commands", self.list_commands_func),
            Command("list commands", "list commands", self.list_commands_func),
            Command("echo", "echo [string]", self.echo_func),
            Command("create_playlist", "create a new project/playlist [name_no_spaces: str] [bpm: int]",
                    self.create_new_playlist),
            Command("cp", "create a new project/playlist [name_no_spaces: str] [bpm: int]",
                    self.create_new_playlist)

            # Command("h", "print help", self.list_commands_func),
            # Command("help", "print help", self.list_commands_func),

        ]

    def run(self):
        self.welcome()
        print()
        while self.running:
            inp: str = input(" : ")
            res = None
            try:
                res = self.exec_string(inp)
            except KeyboardInterrupt as e:
                print("Interrupted. Closing...")
                self.running = False
            except Exception as e:
                print(e)
            Prompt.dbg_print(f"dbg: exit_func code: {res}")

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

    def create_new_playlist(self, options: list) -> int:
        Prompt.dbg_print(f"create_new_playlist options {options}")
        if len(options) != 2:
            print(f"create_new_playlist error! could not parse options, options were: {options}")
            return 1
        name: str = options[0]
        bpm: int = int(options[1])
        print(f"todo send requests to server: {name} {bpm}")
        # self.daw.playlist = Playlist(name, bpm, self.daw.daw_config)
        return 0

    def list_commands_func(self) -> int:
        print("Available Commands: ")
        for command in self.commands:
            print(f"\t{command.command_string} - {command.description}")
        return 0

    def exit_func(self) -> int:
        self.running = False
        print("goodbye :)")
        return 0

    def echo_func(self, string) -> int:
        print(f"hello {string}")
        return 0

    def parse_to_command_options_tuple_list(self, input_string: str) -> list:
        line_list = [line.strip().split(" ") for line in re.split("[;\n]", input_string)]
        parsed_command_options_tuple_list = []
        for line in line_list:
            parsed_command = None
            if len(line) == 0:
                continue
            command_string = line[0]
            if command_string == "":
                continue
            for command in self.commands:
                if command_string == command.command_string:
                    parsed_command = command
            options = []
            if len(line) >= 1:
                options = line[1:]
            parsed_command_options_tuple_list.append((parsed_command, options))
        Prompt.dbg_print(f"parse_to_command_options_tuple_list line_list {line_list}")
        Prompt.dbg_print(
            f"parse_to_command_options_tuple_list parsed_command_options_tuple_list {parsed_command_options_tuple_list}")
        return parsed_command_options_tuple_list

    def exec_string(self, input_string: str) -> int:
        input_command_options_tuple_list = self.parse_to_command_options_tuple_list(input_string)
        if len(input_command_options_tuple_list) == 0:
            return 0
        return_code = 0
        for command_options_tuple in input_command_options_tuple_list:
            command = command_options_tuple[0]
            options = command_options_tuple[1:]
            cmd_return_code = command(options)
            if cmd_return_code != 0:
                return_code = cmd_return_code
        return return_code

    def welcome(self):
        print("welcome")
        self.list_commands_func()


def main(debug: bool = False):
    prompt = Prompt(debug=debug)
    prompt.run()


if __name__ == '__main__':
    typer.run(main)
