#!/bin/zsh
#CLI for common operations such as init, list, write, validate, export
poetry run dynaconf init
poetry run dynaconf -i config.settings list
