"""Test cases for the __main__ module."""
import unittest
from subprocess import SubprocessError

from ibyrd.core.commands._helpers import execute_shell_command


class CommandHelpers(unittest.TestCase):
    """Command Helpers."""

    def test_subprocess_succeeds(self) -> None:
        """test_subprocess_succeeds."""
        output = execute_shell_command("echo test")
        self.assertEqual(output, "test\n")

    def test_subprocess_handles_failures(self):
        """test_subprocess_handles_failures."""
        # No file/directory
        self.assertRaises(FileNotFoundError, execute_shell_command, "fakelocation")

        # Command exited or printed to stderr
        self.assertRaises(SubprocessError, execute_shell_command, "test -e testexit")
