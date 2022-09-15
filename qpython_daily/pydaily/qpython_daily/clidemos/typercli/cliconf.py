#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from enum import Enum


class DefaultCliConfiguration(Enum):
    """
    This class includes all the default values for the application
    """

    APP_NAME = 'typer_qa_cli'
    CONFIGURATION_FILE_NAME = 'json_settings.json'


class CodeOpenerDirectoryPath(Enum):
    COPEN_ROOT_PATH = os.path.dirname(__file__)
    RESOURCE_PATH = os.path.join(COPEN_ROOT_PATH, 'resources')
    CONFIG_FILE_PATH = os.path.join(RESOURCE_PATH, DefaultCliConfiguration.CONFIGURATION_FILE_NAME.value)


