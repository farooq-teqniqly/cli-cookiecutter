from itertools import chain

import pytest
from {{cookiecutter.company_name}}software.cli.main import cli


@pytest.mark.parametrize("expected", chain("clone", "commit", "push"))
def test_git_lists_commands(runner, expected):
    result = runner.invoke(cli, ["git"])
    assert expected in result.output


def test_git_clone_works(runner):
    result = runner.invoke(cli, ["git", "clone", "-sfoo", "-dbar"])
    assert "Cloning repo 'foo' to 'bar'..." in result.output


def test_git_commit_works(runner):
    result = runner.invoke(cli, ["git", "commit", "-mfoo", "-abar"])
    assert "File committed by 'bar'. Commit message: 'foo'" in result.output


def test_git_push_works(runner):
    result = runner.invoke(cli, ["git", "push"])
    assert "Pushing changes to remote..." in result.output
