import click
import sys


class CliOutput:
    def __init__(self):
        self.verbose = False

    @classmethod
    def info(cls, msg, *args):
        """Logs a informational message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def verbose(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            click.echo(msg, *args, file=sys.stderr)
