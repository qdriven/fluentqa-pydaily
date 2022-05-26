#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pathlib import Path

path =Path("../../../docker").cwd()
print(path.absolute())

print(os.getcwd())

# /Users/patrick/workspace/personal/qdriven/fluentqa-pydaily
