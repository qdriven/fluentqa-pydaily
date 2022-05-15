#!/usr/bin/env python
# -*- coding:utf-8 -*-
from invoke import task


@task
def build(c,where,clean=False):
    print(clean)
    print("this is build task")

@task
def clean():
    print("this is clean task")