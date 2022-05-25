#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typer

app = typer.Typer()


@app.command("tag")
def ls_files(tag: str = typer.Option(..., "---tag", "-t",
                                     help="tag labels")):
    typer.echo(f"this is {tag}", )
