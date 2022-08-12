#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygetwindow as pg
import time
import ctypes
import winsound

duration = 100  # milliseconds
freq = 600  # Hz
time_on_window = 0  # Seconds


def timed_fun():
    while True:
        window = pg.getActiveWindow()
        if window.title != "Chrome Remote Desktop - <MY-PC>":
            time_on_window += 1
        if window.title == "Chrome Remote Desktop - <MY-PC>":
            time_on_window = 0
        if time_on_window >= 10:
            top_window = pg.getActiveWindow()
            top_window.close()
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            ctypes.windll.user32.MessageBoxW(0, "GET BACK TO WORK DAVE", "STOP PROCRASTINATING", 0x1000)
            time_on_window = 0
        print(time_on_window)
        time.sleep(1)


if __name__ == '__main__':
    timed_fun()
