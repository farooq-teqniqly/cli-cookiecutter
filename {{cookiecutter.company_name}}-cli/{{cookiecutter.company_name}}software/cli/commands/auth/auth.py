import click

from {{cookiecutter.company_name}}software.cli.core.contextservice import ContextService
from {{cookiecutter.company_name}}software.cli.core.keyvaluestore import KeyValueStore
from {{cookiecutter.company_name}}software.cli.core.logger import CliOutput

LOGGED_IN_USER_KEY = "logged-in-user"


@click.group(["auth"], help="Auth commands.")
def cli():
    pass


@cli.command()
@click.pass_obj
def login(context_service: ContextService):
    """Login to the system."""
    cli_output: CliOutput = context_service.get_cli_output()
    store: KeyValueStore = context_service.get_store()

    username = click.prompt("Username", type=str)
    click.prompt("Password", type=str)

    cli_output.info(f"User '{username}' is logged in.")
    store.set(LOGGED_IN_USER_KEY, username)


@cli.command()
@click.pass_obj
def logout(context_service: ContextService):
    """Log out of the system."""
    cli_output: CliOutput = context_service.get_cli_output()
    store: KeyValueStore = context_service.get_store()

    username = store.get(LOGGED_IN_USER_KEY)[1]

    click.confirm(f"Log out user '{username}'?", abort=True)
    store.remove(LOGGED_IN_USER_KEY)
    cli_output.info(f"Logged out user '{username}'.")
