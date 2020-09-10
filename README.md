# Python CLI Cookiecutter

This document explains how to scaffold a new Python CLI using this 
[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/README.html). 
The cookiecutter leverages the [Click](https://click.palletsprojects.com/en/7.x/) Python library for the CLI functionality.

## Install Cookiecutter

Run ```pip install cookiecutter```

# Scaffold a New CLI Project
1. Open a command prompt and switch to the location where you want the project to reside.
2. Create a new virtual environment. 
2. Run ```cookiecutter https://github.com/farooq-teqniqly/cli-cookiecutter```
3. Enter the company name. This will be used in the various folder names and in the README.
4. Enter the CLI's description. This description will be shown in the module's README.
5. Enter your e-mail address. This will be put in ```setup.py```.
6. Right-click the **tests** folder and select **Run Unittests in tests**. The sole test should pass.

That's it, start coding your module!

# Contributing

Contributions are welcome. Just follow the same process as you do for other repos.