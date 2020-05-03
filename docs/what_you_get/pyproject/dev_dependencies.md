# Dev Dependencies
These are all the packages that this cookiecutter will include for your project to use for development and CI.
 These things will not be included in your packaged Lambda function at runtime.
 The relevant section in `pyproject.toml` is highlighted below for reference.

1. [uvicorn]: Used to run locally for development because running serverless offline is hard and buggy.
1. [pytest]: A testing framework.
1. [mypy]: Static type checking.
1. [sqlalchemy-stubs]: Allows for static type checking of SQLAlchemy models.
1. [safety]: Check your dependencies for vulnerabilities.
1. [black]: Auto-formatter for your Python code.
1. [taskipy]: Define useful shortcuts for running tasks in your Poetry environment.
1. [isort]: Automatically sort your dependencies.
1. [pytest-cov]: Easily collect coverage statistics while running pytest.
1. [typer]: "The FastAPI of CLIs" for managing utilities for your app.
1. [alembic]: Generates and runs database migrations for SQLAlchemy models.

```toml hl_lines="31 32 33 34 35 36 37 38 39 40 41 42"
{!../example/pyproject.toml!}
```

[uvicorn]: https://www.uvicorn.org/
[pytest]: https://docs.pytest.org/en/latest/
[mypy]: http://mypy-lang.org/
[sqlalchemy-stubs]: https://github.com/dropbox/sqlalchemy-stubs
[safety]: https://pypi.org/project/safety/
[black]: https://black.readthedocs.io/en/stable/
[pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/
{!./hyperlinks.md!}
