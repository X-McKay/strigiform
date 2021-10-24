"""Test cases for the cli module."""
import pytest
from click.testing import CliRunner

from kingfisher.core.cli import main


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(main)
    assert result.exit_code == 0
