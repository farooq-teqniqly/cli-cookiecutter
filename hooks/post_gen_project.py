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

print(paths)

# Folder names in lowercase.
for path in paths:
    os.rename(path, path.lower())

source_files = [
    path
    for path in glob.glob("./**/*.py", recursive=True)
    if path.__contains__(".py")
]

print(source_files)

for file in source_files:
    with open(file, "r") as f:
        contents = f.read()

        # imports in lowercase
        contents = contents.replace(
            "{{cookiecutter.company_name}}", "{{cookiecutter.company_name}}".lower()
        )

        # class names in CamelCase.
        contents = contents.replace(
            f"class {{cookiecutter.company_name}}".lower(),
            "class {{cookiecutter.company_name}}",
        )

        # replace description text with original in case it contained the company name
        contents = contents.replace(
            f"help={{cookiecutter.cli_description}}".lower(),
            "help={{cookiecutter.cli_description}}",
        )

    with open(file, "w+") as f:
        f.write(contents)
