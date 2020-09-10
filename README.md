# Python CLI Cookiecutter

This document explains how to scaffold a new Python CLI using this 
[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html). 
The cookiecutter leverages the [Click](https://click.palletsprojects.com/en/7.x/) Python library for the CLI functionality.

## Install Cookiecutter

Run ```pip install cookiecutter```

# Scaffold a New CLI Project
1. Open a command prompt and switch to the location where you want the project to reside.
2. Run ```cookiecutter https://github.com/farooq-teqniqly/cli-cookiecutter```
3. Enter a name for the CLI's executable.
4. Enter the company name. This name should be in CamelCase. This will be used in the various folder names, 
the README, and the LICENSE files.
5. Enter the CLI's description. This description will be shown in the README.
6. Enter your e-mail address. This will be put in ```setup.py```.

# Run the CLI Tests
The cookiecutter scaffolds a simple CLI that exhibits some of Click's interesting features. Prior to running the CLI,
verify all tests pass:

1. Switch to the folder named ```[Company Name]-cli```.
2. Create and activate a new virtual environment:
   - Run ```python -m venv .```
   - Run ```Scripts\activate.bat```
3. Run ```pip install -r requirements.txt```.
4. Run ```pytest``` and verify all 20 tests pass.

# Install the CLI
1. Run ```pip install --editable .``` This will install the CLI using ```setup.py```.
2. Enter the name of the CLI's executable and press ENTER. The default executable name is ```cl```. Assuming you 
selected default values for the other parameters, you should see the following help output:

```
Usage: cl [OPTIONS] COMMAND [ARGS]...

  My CLI does interesting stuff.

Options:
  --help  Show this message and exit.

Commands:
  auth  Auth commands.
  git   Git commands.
```

# Code Layout
Type ```cl git``` and press enter. You should see the following output:

```
Usage: cl git [OPTIONS] COMMAND [ARGS]...

  Git commands.

Options:
  -h, --home TEXT  The repository directory.
  -d, --debug      Turn on debug mode.
  --help           Show this message and exit.

Commands:
  clone   Clone a repository.
  commit  Commit local changes.
  push    Push changes to remote.
```

In this context, ```git``` is a command **group**. The ```git``` command group consists of three commands - 
clone, commit, and push. Open ```git.py``` and observe there is a function for each command.

# Click Features
Most of the commands in the cookiecutter template show off a feature of Click.

## git clone
Shows how to configure a command with required arguments.

## git commit
Shows how to access an object added to Click's context. This is used to provide arguments that are applicable
to all commands, i.e. ```--home``` and ```--debug```.

## git push
Shows how to write output to the console. The ```CliOutput``` class is an abstraction over ```click.echo()```.

# State Management

When a CLI command is executed, a new process is started, the command runs, and the process exits. You may want to share
information between command executions. There is an abstract ```StateService``` class that can be used to create your
own state manager. The cookiecutter provides a SQLLite based state manager in ```sqllitestateservice.py```.

The ```auth``` command group demonstrates use of the ```SqlLiteStateService```. The user's context is saved by ```auth login```
and removed by ```auth logout```.

# Contributing

Contributions are welcome. Just follow the same process as you do for other repos.