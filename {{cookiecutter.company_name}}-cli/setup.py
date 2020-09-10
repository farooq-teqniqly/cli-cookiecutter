import setuptools
import os

# Change to the setup.py directory to read files relative to it.
cwd = os.getcwd()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="{{cookiecutter.company_name}}-CLI",
    version=1.0,
    author="{{cookiecutter.company_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_namespace_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["click==7.1.2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["{{cookiecutter.cli_executable_name}}={{cookiecutter.company_name}}software.cli.main:cli"]}
)

# Pop back to the original directory.
os.chdir(cwd)
