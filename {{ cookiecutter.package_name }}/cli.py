import json
import typer

cli = typer.Typer()


@cli.callback()
def callback(
):
    """
    CLI for managing {{ cookiecutter.package_name }}
    """


@cli.command()
def openapi():
    """ Generate an openapi.json """
    from {{ cookiecutter.module_name }}.main import app
    from pathlib import Path

    spec = app.openapi()
    p = Path("openapi.json")
    p.write_text(json.dumps(spec))
