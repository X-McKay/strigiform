"""Cli interface for Launching webapp."""
import os

import click

from ibyrd.core.commands._helpers import execute_shell_command


def launch_vault_cmd(vault_config_dir="./src/ibyrd/secrets/vault_config.hcl"):
    """Launch HashiCorp Vault."""
    # TODO: Check server status before attempting
    vault_cmd = "vault server -config=./src/ibyrd/secrets/vault_config.hcl"
    if os.path.isfile(vault_config_dir) is False:
        raise FileNotFoundError
        exit
    click.secho("Starting Vault!")
    execute_shell_command(vault_cmd)
