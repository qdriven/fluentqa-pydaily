#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typer

import ls_command

app = typer.Typer(name='cmd')
app.add_typer(ls_command.app, name="ls")


def main():
    typer.echo("typer information:")


if __name__ == '__main__':
    app()
