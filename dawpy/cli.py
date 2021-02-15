from dawpy._version import __version__
import typer
from dawpy.shell import Shell
from typing import Optional

app = typer.Typer()
shell_app = typer.Typer()
app.add_typer(shell_app, name="shell")


def version_callback(value: bool):
    """ displays the current version """
    if value:
        typer.echo(f"dawpy version: {__version__}")
        raise typer.Exit()


@shell_app.callback(invoke_without_command=True)
@shell_app.command()
def shell(
    script_path: str = typer.Option(None),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback
    ),
):
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
    typer.run(shell)


def main():
    cli()


if __name__ == "__main__":
    main()
