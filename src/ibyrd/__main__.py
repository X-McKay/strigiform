"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """ibyrd."""


if __name__ == "__main__":
    main(prog_name="ibyrd")  # pragma: no cover
