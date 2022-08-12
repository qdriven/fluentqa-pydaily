#!/usr/bin/env python
# -*- coding:utf-8 -*-
from smtplib import SMTP

# todo:
# 1. getting default sender addr/password
# 2. cli parameter override default sender
# 3. msg: default as got it as templates

def send_email(server: SMTP, sender_addr, rec_addr, msg, pwd, **kwargs):
    # server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_addr, pwd)
    server.sendmail(sender_addr, rec_addr, msg)
    print("Mail sent successfully....!")
