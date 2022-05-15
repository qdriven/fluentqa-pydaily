#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from dotenv import load_dotenv

env_vars = load_dotenv()

print(env_vars)
print(os.getenv("test"))
print(os.getenv("temp.nice"))