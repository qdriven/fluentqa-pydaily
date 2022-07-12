#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Feature	Dataclass	Attrs	Pydantic
# frozen	✅	✅	✅
# defaults	✅	✅	✅
# totuple	✅	✅	✅
# todict	✅	✅	✅
# validators	❌	✅	✅
# converters	❌	✅	✅
# slotted	❌	✅	❌
# programmatic creation	❌	✅	❌
#
# When to use Dataclasses
# Dataclasses are mainly about 'grouping' variables together. Choose dataclasses if:
#
# The main concern is around the type of the variable, not the value
# Adding another package dependancy isn't trivial
# When to use Attrs
# Attrs are about both grouping & validating. Choose attrs if:
#
# You're concerned around the performance (attrs supports slotted class generation which are optimized for CPython)
# When to use Pydantic
# Pydantic is about thorough data validation. Choose pydantic if:
#
# You want to validate the values inside each class
# You want to santise the input


def class_tester(class_constructor):
    test_class_1 = class_constructor()
    test_class_2 = class_constructor()

    print(f"Repr/str dunder method representation: {test_class_1}")

    print(f"Equality dunder method (using ==) (should be True if implemented): {test_class_1 == test_class_2}")

    print(f"Equality dunder method (using is) (should be True if implemented): {test_class_1 is test_class_2}")
