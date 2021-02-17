from pydantic.typing import NoneType
from dawpy._version import __version__
from dawpy.shell import Shell
from typing import Optional
import sys
import argparse


def shell(script_path: str = ""):
    """ start the dawpy shell """
    dps = Shell()
    if script_path:
        with open(script_path, "r") as f:
            commands = f.readlines()
            dps.cmdqueue.extend(commands)
    dps.cmdloop()
    print("shut down correctly")


def cli():
    """ run the dawpy cli """
    sys.argv = [x for x in sys.argv if x is not None and ".py" not in x]
    parser = argparse.ArgumentParser(
        prog="dawpy", description="Python based Digital Audio Workstation"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="dawpy " + __version__,
        help="Show the dawpy version number and exit.",
    )

    subparsers = parser.add_subparsers(help="run a dawpy subcommand")

    shell_parser = subparsers.add_parser(
        "shell", help="Start the REPL DawpyShell (dsh)"
    )
    shell_parser.add_argument(
        "-s", "--script", dest="shell_script", help="run a dawpy-shell script (.dsh)"
    )
    shell_parser.add_argument(
        "-c", "--command", dest="shell_command", help="run a dawpy-shell command"
    )

    shell_parser.set_defaults(shell=True)
    args = parser.parse_args(sys.argv)
    if len(vars(args)) == 0:
        shell()
    elif args.shell:
        shell(args.shell_script)
    else:
        print("ERROR NO ARGS")


def main():
    cli()


if __name__ == "__main__":
    main()
