"""Cli interface for Nox testing."""
import os

import click

from strigiform.core.commands._helpers import execute_shell_command


def get_root_dir():
    """Return root directory of project."""
    return os.path.dirname(os.path.abspath("src"))


root_dir = get_root_dir()


def nox_cmd(root_dir: str = root_dir):
    """Runs entire Nox test suite."""
    test_script = os.path.join(root_dir, "bin/test")
    if os.path.isfile(test_script) is False:
        raise FileNotFoundError
        exit
    click.secho("Running testing suite!")
    execute_shell_command(test_script)
