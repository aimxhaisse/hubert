import typer


app = typer.Typer()


@app.command()
def train():
    """
    Train Hubert.
    """
    typer.echo("Training Hubert")
