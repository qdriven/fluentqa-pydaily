#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydaily.lessons.translation_demo.fluent_translators import ZhTranslator


def test_translate_batch():
    assert False


def test_translate_file():
    file_name="readme.md"
    translater = ZhTranslator()
    texts ="""Testing is an essential phase in any product life cycle; whether if it's a food, cars, or software production line, the outcomes should match what's expected and meet, satisfy the need that we created the product for.
Having a solid base of understanding how the software components work and integrate with each other as well as gaining the skills of breaking things is an essential skill-set for any QA engineer. Software testing is the art of investigating the software and finding any unintended behavior that might generate undesired scenarios.
Below you can find the path for QA and software testing learning curve which you might need to start the journey.
"""
    result =translater.translator.translate(texts)
    print(result)