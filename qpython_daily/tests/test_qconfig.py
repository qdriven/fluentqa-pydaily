#!/usr/bin/env python
# -*- coding:utf-8 -*-
from qpython_daily.qconfig import qsettings


def test_settings():
    assert qsettings.key == "value"
    assert qsettings.number == 1234
    assert qsettings.a_dict.nested.other_level == "nested value"
    assert qsettings['a_boolean'] is False
    assert qsettings.get("DONTEXIST", default=1) == 1
    print(qsettings.DB_NAME)
