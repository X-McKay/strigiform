"""Cli interface for Launching webapp."""
import os

import click

from strigiform.core.commands._helpers import execute_shell_command


def launch_app_cmd(app_dir="src/strigiform/app/streamlit.py"):
    """Launch webapp."""
    launch_cmd = "streamlit run src/strigiform/app/streamlit.py"
    if os.path.isfile(app_dir) is False:
        raise FileNotFoundError
        exit
    click.secho("Launching webapp!")
    execute_shell_command(launch_cmd)
