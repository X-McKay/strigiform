"""Cli interface for Nox testing."""
import os

import click

from ibyrd.core.commands._helpers import execute_shell_command


def test_cmd(root_dir: str):
    """Runs entire Nox test suite."""
    test_script = os.path.join(root_dir, "bin/test")
    click.echo("Running testing suite!")
    execute_shell_command(test_script)
