"""
This runs after the cookiecutter has laid out the file structure.
"""
import os
import glob

module_folder = os.getcwd()

paths = [
    path
    for path in glob.glob("./**/*", recursive=True)
    if path.__contains__("{{cookiecutter.company_name}}")
]

# Folder names in lowercase.
for path in paths:
    os.rename(path, path.lower())

source_files = [
    path
    for path in glob.glob("./**/*.py", recursive=True)
    if path.__contains__("{{cookiecutter.company_name}}.py".lower())
]


for file in source_files:
    with open(file, "r") as f:
        contents = f.read()

        # imports in lowercase
        contents = contents.replace(
            "{{cookiecutter.company_name}}", "{{cookiecutter.company_name}}".lower()
        )

    with open(file, "w+") as f:
        f.write(contents)