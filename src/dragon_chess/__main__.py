"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Dragon Chess."""


if __name__ == "__main__":
    main(prog_name="dragon-chess")  # pragma: no cover
