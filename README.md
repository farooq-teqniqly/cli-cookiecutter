# Python CLI Cookiecutter

This document explains how to scaffold a new Python CLI using this 
[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html). 
The cookiecutter leverages the [Click](https://click.palletsprojects.com/en/7.x/) Python library for the CLI functionality.

## Install Cookiecutter

Run ```pip install cookiecutter```

# Scaffold a New CLI Project
1. Open a command prompt and switch to the location where you want the project to reside.
2. Create a new virtual environment. 
3. Run ```cookiecutter https://github.com/farooq-teqniqly/cli-cookiecutter```
4. Enter a name for the CLI's executable.
5. Enter the company name. This will be used in the various folder names, the README, and the LICENSE files.
6. Enter the CLI's description. This description will be shown in the README.
7. Enter your e-mail address. This will be put in ```setup.py```.

# Run the CLI Tests
The cookiecutter scaffolds a simple CLI that exhibits some of Click's interesting features. Prior to running the CLI,
verify all tests pass:

1. Switch to the folder containing the ``requirements.txt`` file.
2. Create and activate a new virtual environment.
3. Run ```pip install -r requirements.txt```.
4. Run ```pytest``` and verify all 20 tests pass.

# Run the CLI


# Contributing

Contributions are welcome. Just follow the same process as you do for other repos.