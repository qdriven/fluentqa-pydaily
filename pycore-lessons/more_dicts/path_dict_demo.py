#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pathdict import PathDict

db = {
    "bob": {
        "interests": {
            "sports": ["soccer", "basketball"]
        }
    },
    "julia": {
        "interests": {
            "music": ["pop", "alternative"]
        }
    }
}
for user_name in db:
    user_music = None
    if user_name in db:
        if "interests" in db[user_name]:
            if "music" in db[user_name]["interests"]:
                user_music = db[user_name]["interests"]["music"]
    print(user_music)

# ---> None
# ---> ["pop", "alternative"]

db = PathDict(db)
for user_name in db:
    print(db[user_name, "interests", "music"])

# ---> None
# ---> ["pop", "alternative"]
# https://github.com/mkrd/PathDict