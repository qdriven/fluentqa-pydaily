#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from abc import ABC
from typing import TextIO


class QPluginMeta(ABC):
    pass


class QPlugin(metaclass=QPluginMeta):
    def print(self, msg: str, file: TextIO = sys.stdout, **kwargs) -> None:
        """
        Print a message.
        All kwargs of regular 'print' are supported.
        @param msg: The message to print.
        @param file: The destination IO stream where the message is printed on (Default: stdout).
        """
        self.__print(msg, out=file, **kwargs)

    def __print(self, msg: str, out: TextIO = sys.stdout, **kwargs) -> None:
        # insert the plugin name before the message
        print("[%s]: %s" % (self.plugin_name, msg), file=out, **kwargs)

    def eprint(self, msg: str, file: TextIO = sys.stderr, **kwargs) -> None:
        """
        Print a message.
        All kwargs of regular 'print' are supported.
        @param msg: The message to print.
        @param file: The destination IO stream where the message is printed on (Default: stderr).
        """
        self.__print(msg, out=file, **kwargs)

    @property
    def plugin_name(cls) -> str:
        """
        Get the name of the plugin.
        By default the class name is used.
        """
        return cls.__name__
