#!/usr/bin/env python

from fluentcli.cleo_demo.cleo_command import GreetCommand
from cleo import Application

application = Application()
application.add(GreetCommand())

def main():
    application.run()


if __name__ == '__main__':
    main()