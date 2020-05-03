# Dependencies
These are all the packages that this cookiecutter will include for your project to use at runtime. The relevant section 
in `pyproject.toml` is highlighted below for reference.

1. [fastapi]: The basis for your whole project!
1. [mangum]: The key to getting FastAPI running in Lambda
1. [sqlalchemy]: An ORM- the best fully-featured ORM we've found.
1. [alembic]: For managing database migrations with SQLAlchemy
1. [pymysql]: A MySQL driver for Python- required to hook up SQLAlchemy to MySQL
1. `triax-flex-config`: A package we developed to make configuring web apps easier.
1. [semantic-version]: Python does some weird stuff with your project version- we use this to make the published 
    version (in the OpenAPI document) follow standard [Semantic Versioning](https://semver.org/).
1. [markdown]: For publishing CHANGELOG.md with the API so consumers can know what's going on.
1. [secure]: For setting some security settings (e.g. HSTS header in responses)

```toml hl_lines="19 21 22 23 24 25 26 27 28"
{!../example/pyproject.toml!}
```

[mangum]: https://erm.github.io/mangum/introduction/
[sqlalchemy]: https://www.sqlalchemy.org/
[pymysql]: https://pymysql.readthedocs.io/en/latest/
[semantic-version]: https://python-semanticversion.readthedocs.io/en/latest/
[markdown]: https://python-markdown.github.io/
[secure]: https://secure.readthedocs.io/en/latest/
{!./hyperlinks.md!}
