#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


def clean_photo():
    for (dirname, dirs, files) in os.walk(''):
        for filename in files:
            if filename.endswith('.txt'):
                thefile = os.path.join(dirname, filename)
                size = os.path.getsize(thefile)
                if size == 2578 or size == 2565:
                    print(thefile)
                    # os.remove(thefile) Add this when you are sure to delete the file
                    continue
                with open(thefile, 'r') as fhand:
                    lines = list()
                    for line in fhand:
                        lines.append(line)
                if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
                    print(thefile)
                    # os.remove(thefile) Add this when you are sure to delete the file
                    continue
