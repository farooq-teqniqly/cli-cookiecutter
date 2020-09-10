import click
import glob
import os

from {{cookiecutter.company_name}}software.cli.core.contextservice import ContextService
from {{cookiecutter.company_name}}software.cli.core.logger import CliOutput
from {{cookiecutter.company_name}}software.cli.core.sqllitekeyvaluestore import SqlLiteKeyValueStore

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class {{cookiecutter.company_name}}Cli(click.MultiCommand):
    @classmethod
    def list_commands(cls, ctx):
        rv = []

        glob_exp = os.path.join(cmd_folder, "**")
        for filepath in glob.glob(glob_exp, recursive=True):
            filename = filepath.split(os.sep)[-1]

            if filename.startswith("_"):
                continue
            if filename.endswith(".py"):
                rv.append(filename[:-3])

        rv.sort()
        return rv

    @classmethod
    def get_command(cls, ctx, cmd_name):
        ns = {}
        filename = os.path.join(cmd_folder, cmd_name, cmd_name + ".py")

        with open(filename) as f:
            code = compile(f.read(), filename, "exec")
            eval(code, ns, ns)

        return ns["cli"]


@click.group(cls={{cookiecutter.company_name}}Cli, help="{{cookiecutter.cli_description}}")
@click.pass_context
def cli(ctx: click.Context):
    store = SqlLiteKeyValueStore()
    store.initialize()
    ctx.obj = ContextService(dict(log=CliOutput(), store=store))


if __name__ == "__main__":
    cli()
