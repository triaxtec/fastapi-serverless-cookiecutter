# Private PyPI Repo
The section of `pyproject.toml` that starts with `[[tool.poetry.source]]` (highlighted below) is where you can set up 
a private PyPI repository to install Python packages from. Everything in this project supports using private repositories 
registered somewhere like [Gemfury]. If you don't need this feature, delete that section from `pyproject.toml`.



```toml hl_lines="15 16 17"
{!../example/pyproject.toml!}
```

{!./hyperlinks.md!}
