# Next Steps
So you've generated yourself a new project with this cookiecutter... what now? Well the first thing you need to handle 
is your private repository settings.

#### If you're using private repositories:
1. Set your credentials in [Poetry] if you haven't done so previously using the following two commands, substituting 
 your own URL and credentials:
    1. `poetry config repositories.private https://pypi.fury.io/my-org/`
    1. `poetry config http-basic.private "$GEMFURY_PULL_TOKEN" "$GEMFURY_PULL_TOKEN"`

#### If you are not using private repositories
Remove anything that references private repositories in:

1. [pyproject.toml](what_you_get/pyproject/private_pypi.md)
1. [CircleCI Config](what_you_get/circleci.md)
1. [Angular Client Config](what_you_get/generator_config.md)

Now that that's done- it's time to install some dependencies! Go to your freshly generated directory and run 
 `poetry install` to install both regular and dev dependencies. Now hop into a `poetry shell` so you can run other 
 commands without prefixing them with `poetry run`.
 
## Run the project locally
Let's make sure everything is hunky dory and see what it is you've generated.

### Run MySQL
This project generator assumes you'll be using MySQL with SQLAlchemy for your database. If that's not the case, you've got 
some tweaking to do. If you are using that setup, you need to be running a MySQL database locally in order to run tests 
or the services themselves. There are a million ways to run MySQL so I'll leave it up to you to decide how you're going 
to do that.

Once you've got it running, create two databases. The first should be called "testing" (used by unit tests). The second 
should be named the same as your project. Check out the generated `sample-config.yml` to see what exactly it's expecting.

### Run the checks
Now that your testing database exists, you should be able to run `task check` and see everything pass. It's possible 
[isort] and [black] will have a bit of work to do as formatting templates is tricky.

### Set some config values
Before you can run this thing for real, you have to create a `config.yml` in the root of the project. [flex-config] 
requires some source to set the database credentials, and the easiest way to do that locally is via YAML. So copy 
`sample-config.yml` to `config.yml` and adjust values as needed.

### Run the thing!
To run your API locally now, do `uvicorn <module_name>.main:app`. You should be able to go to 
[http://localhost:8000/docs](http://localhost:8000/docs) to see your fresh new API.



{!./hyperlinks.md!}
