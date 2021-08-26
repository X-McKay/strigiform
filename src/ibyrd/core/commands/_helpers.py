"""Helpers for Click CLI."""
import shlex
import subprocess
import traceback
from enum import Enum
from subprocess import SubprocessError
from typing import Optional

import click


class CliColors(Enum):
    """Defining Cli color codes."""

    USAGE = "yellow"
    OPTIONS = "green"
    ERROR = "red"
    INFO = "white"
    HEADER = "blue"


class CliUnicode(Enum):
    """Cli unicode configuration."""

    bullet = "\u2022"


def execute_shell_command(command: str) -> Optional[str]:
    """Executes shell command in interactive mode."""
    try:
        with subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE) as process:
            paths = []
            while True:
                output = process.stdout.readline().decode()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    paths.append(output)
                    click.secho(output.strip())
            stdout, stderr = process.communicate()
            rc = process.returncode
            if rc != 0 or stderr is not None:
                raise SubprocessError(stderr)
            return None if len(paths) == 0 else paths[0]
    except (SubprocessError, FileNotFoundError):
        e_string = traceback.format_exc()
        click.secho(f"Command {command} failed due to: ", fg=CliColors.ERROR.value)
        click.secho(e_string, fg=CliColors.ERROR.value)
        raise
