import click

from {{cookiecutter.company_name}}software.cli.core.contextservice import ContextService
from {{cookiecutter.company_name}}software.cli.core.logger import CliOutput
from {{cookiecutter.company_name}}software.cli.core.repo import Repo


@click.group(["git"], help="Git commands.")
@click.option("-h", "--home", help="The repository directory.")
@click.option("-d", "--debug", is_flag=True, help="Turn on debug mode.")
@click.pass_context
def cli(ctx, home: str, debug: bool):
    ctx.obj.add("repo", Repo(home, debug))


@cli.command()
@click.option("-s", "--source", required=True, help="The source repository.")
@click.option("-d", "--destination", required=True, help="The local path.")
@click.pass_obj
def clone(context_service: ContextService, source: str, destination: str):
    """Clone a repository."""
    cli_output: CliOutput = context_service.get_cli_output()
    cli_output.info(f"Cloning repo '{source}' to '{destination}'...")


@cli.command()
@click.option("-m", "--message", required=True, help="Commit message.")
@click.option("-a", "--author", required=True, help="The author.")
@click.pass_obj
def commit(context_service: ContextService, message: str, author: str):
    """Commit local changes."""
    repo: Repo = context_service.get("repo")
    cli_output: CliOutput = context_service.get_cli_output()

    cli_output.info(f"File committed by '{author}'. Commit message: '{message}'")

    if repo.debug:
        cli_output.info(repr(repo))


@cli.command()
@click.pass_obj
def push(context_service: ContextService):
    """Push changes to remote."""
    cli_output: CliOutput = context_service.get_cli_output()
    cli_output.info("Pushing changes to remote...")
