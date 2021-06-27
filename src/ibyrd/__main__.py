"""Command-line interface."""
import click


@click.command()
def main() -> None:
    """ibyrd."""
    click.echo("Hello, Birders!")


if __name__ == "__main__":
    main(prog_name="ibyrd")
