# pyproject.toml
The single source of metadata for your project, as defined by PEP-518. This contains configuration for several tools used in building & testing your app.

## [Poetry]
Used to manage dependencies, and virtual environments. It can also be used to build/publish packages, but you likely 
won't be needing those features for this project.

#### [Private PyPI Repository](pyproject/private_pypi.md)
Configure a private PyPI repo that you can install dependencies from.       

#### [Dependencies](pyproject/dependencies.md)
The Python packages your project will use at runtime

#### [Dev Dependencies](pyproject/dev_dependencies.md)
The Python packages only you and CI use, not packaged with a release

#### [CLI Entrypoint](pyproject/cli.md)
An entrypoint to a CLI named the same thing as the [module_name](../README.md#module_name) variable for calling the [Typer]
 CLI defined in [cli.py](cli.md).

## [taskipy](pyproject/taskipy.md)
A tool for easily running commands in the context of our [Poetry] environment.

## [black](pyproject/black.md)
Automatically reformats your code.

## [isort](pyproject/isort.md)
Organizes your Python imports.

## [coverage](pyproject/coverage.md)
Configure [Coverage].

{!./hyperlinks.md!}
