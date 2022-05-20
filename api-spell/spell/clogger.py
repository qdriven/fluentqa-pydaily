#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from loguru import logger as clogger

from spell.config import settings

LOG_LEVEL = settings.log_level
LOG_FILE_PATH=settings.log_file_path
clogger.add(sys.stderr, format="{time} {level} {message}",level=LOG_LEVEL)
clogger.add(LOG_FILE_PATH, backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

clogger.info("current log level is {}",LOG_LEVEL)