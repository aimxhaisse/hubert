import subprocess
import typer

from . import Hubert


app = typer.Typer()


@app.command()
def autocomplete(input_file: str):
    """
    Given an input text, autocompletes.
    """
    with open(input_file, 'r') as f:
        h = Hubert
        click.echo(h.autocomplete(f.read()))


@app.command()
def train():
    """
    Train Hubert.
    """
    typer.echo("Training Hubert")


@app.command()
def test():
    """
    Run all unittests.
    """
    subprocess.run(
        ['python', '-u', '-m', 'unittest', 'discover']
    )
