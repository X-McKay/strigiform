"""Test cases for the commands module."""
import os
import unittest
from subprocess import SubprocessError

from strigiform.core.commands._helpers import execute_shell_command
from strigiform.core.commands.hotspots import clean_echo_results
from strigiform.core.commands.hotspots import hotspot_cmd
from strigiform.core.commands.test import get_root_dir
from strigiform.core.commands.test import nox_cmd


class CommandHelpers(unittest.TestCase):
    """Command Helpers."""

    def test_subprocess_succeeds(self) -> None:
        """test_subprocess_succeeds."""
        output = execute_shell_command("echo test")
        self.assertEqual(output, "test\n")

    def test_subprocess_handles_failures(self) -> None:
        """test_subprocess_handles_failures."""
        # No file/directory
        self.assertRaises(FileNotFoundError, execute_shell_command, "fakelocation")

        # Command exited or printed to stderr
        self.assertRaises(SubprocessError, execute_shell_command, "test -e testexit")

    def test_get_root_dir(self) -> None:
        """Test function to extract root_dir."""
        secondary_dir = os.path.dirname(os.path.abspath("docs"))
        self.assertEqual(get_root_dir(), secondary_dir)

    def test_nox_cmd(self) -> None:
        """Test for strigiform test cli command."""
        self.assertRaises(FileNotFoundError, nox_cmd, "fake")

    def test_hotspots(self) -> None:
        """Test for strigiform hotspot cli command."""
        self.assertRaises(ValueError, hotspot_cmd, lat=100)

    def test_clean_echo_results(self) -> None:
        """Test for echo of hotspots to terminal."""
        data = [
            {
                "locName": "Location 1",
                "countryCode": "US",
                "latestObsDt": "2021-06-11 06:30",
            },
            {"countryCode": "US"},
        ]

        self.assertRaises(KeyError, clean_echo_results, data)
