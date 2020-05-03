# Tasks
The `[tool.taskipy.tasks]` section (highlighted below) uses [taskipy] to define shortcuts to commands that will run
 in your [Poetry] environment. When in a `poetry shell`, these commands can be run like `task <command_name>`. The 
 commands included in this cookiecutter are:

1. `migrate`: Uses [alembic] to generate a new migration like `task migrate a_description_here`.
1. `upgrade`: Runs any missing migrations on your local database.
1. `downgrade`: Undoes the last migration run on your local database.
1. `upgrade_dev`: Just like `upgrade` but sets the value of "env" in [config](../module/config.md) to "dev" so that 
 your database URL for your "dev" environment can be loaded from [AWS SSM].
1. `downgrade_dev`: Just like `downgrade` but sets the value of "env" in [config](../module/config.md) to "dev" so that 
 your database URL for your "dev" environment can be loaded from [AWS SSM].
1. `upgrade_live`: Just like `upgrade` but sets the value of "env" in [config](../module/config.md) to "live" so that 
 your database URL for your "live" environment can be loaded from [AWS SSM].
1. `downgrade_live`: Just like `downgrade` but sets the value of "env" in [config](../module/config.md) to "live" so that 
 your database URL for your "live" environment can be loaded from [AWS SSM].
1. `check`: Runs the same checks that CI will run, but applies fixes where it can (formatting). Run before each commit
 to save yourself a bit of pain.
 


```toml hl_lines="47 48 49 50 51 52 53 54 55"
{!../example/pyproject.toml!}
```

{!./hyperlinks.md!}
