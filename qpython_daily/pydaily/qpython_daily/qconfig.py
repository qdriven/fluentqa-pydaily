#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dynaconf import Dynaconf

qsettings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    load_dotenv=True,
    ignore_unknown_envvars=True
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
