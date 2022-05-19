#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typer

cli = typer.Typer()


@cli.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@cli.command()
def bye(name: str, formal: bool = False):
    typer.echo(f"bye,{name}")


if __name__ == '__main__':
    cli()
