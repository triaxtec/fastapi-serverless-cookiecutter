# CLI Entrypoint
The `[tool.poetry.scripts]` section (highlighted below) allows you to create entrypoints into your package. In this case
 we define an entrypoint to the [Typer] CLI declared in [cli.py](../cli.md). This means with a package called "example" 
 we can do `poetry run example` to access that [Typer] CLI. In the case of the generated CLI, this enables us to run
 `poetry run example openapi` in order to generate an `openapi.json` file to be used for Client Generation in CI.


```toml hl_lines="44 45"
{!../example/pyproject.toml!}
```

{!./hyperlinks.md!}
