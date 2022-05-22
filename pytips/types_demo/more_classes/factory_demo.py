#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass


class Apple(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")


class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")


class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        print("create new class")
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()

    def __init__(self,name):
        print("init stage")
        self.name=name


fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit1.print_color()
fruit2.print_color()

print(FruitFactory(name="name")) # error