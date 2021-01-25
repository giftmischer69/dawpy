# here a typer application
import typer
from dawpy.shell import Shell
from typing import Optional

app = typer.Typer()
shell_app = typer.Typer()
app.add_typer(shell_app, name="shell")


# TODO: HERE
# add command with hidden = true for a sick hardcoded project maybe


@shell_app.callback(invoke_without_command=True)
@shell_app.command()
def shell(script_path: str = None):
    """ start the dawpy shell """
    dps = Shell()
    if script_path:
        with open(script_path, "r") as f:
            commands = f.readlines()
            dps.cmdqueue.extend(commands)
    dps.cmdloop()
    print("shut down correctly")


def cli():
    app()


if __name__ == "__main__":
    cli()
