#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typer

import cmd


def main():
    typer.echo("typer information:")
    typer.echo(cmd.__name__)
    typer.echo(cmd.__version__)


if __name__ == '__main__':
    typer.run(main)