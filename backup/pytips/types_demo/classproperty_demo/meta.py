#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional


class ClassProperty(property):
    """
    The use this class as a decorator for your class property.

    Example:
        @classproperty
        def prop(cls):
            return "value"
    """

    def __get__(self, *args, **kwargs):
        """
         This method gets called when a property value is requested.
         @return: The value of the property.
         """
        # apply the __get__ on the class, which is the second argument
        super(ClassProperty, self).__get__(args[1])

    def __set__(self, cls_or_instance, value: object) -> None:
        """
        This method gets called when a property value should be set.
        @param cls_or_instance: The class or instance of which the property should be changed.
        @param value: The new value.
        """
        # call this method only on the class, not the instance
        super(ClassProperty, self).__set__(self.get_class(cls_or_instance), value)

    def __delete__(self, cls_or_instance) -> None:
        """
        This method gets called when a property should be deleted.
        @param cls_or_instance: The class or instance of which the property should be deleted.
        """
        # call this method only on the class, not the instance
        super(ClassProperty, self).__delete__(self.get_class(cls_or_instance))

    @staticmethod
    def get_class(cls_or_instance):
        if isinstance(cls_or_instance, type):
            return cls_or_instance
        else:
            return type(cls_or_instance)


class ClassPropertyMeta(type):

    def __get_classprop_attr(self, name: str) -> Optional[ClassProperty]:
        if (name in self.__dict__ and
                isinstance(self.__dict__[name], ClassProperty)):
            return self.__dict__[name]
        else:
            return None

    def __setattr__(self, key: str, value: object) -> None:
        cp_obj: Optional[ClassProperty] = self.__get_classprop_attr(key)
        if cp_obj:
            cp_obj.__set__(self, value)
        else:
            super(ClassPropertyMeta, self).__setattr__(key, value)

    def __delattr__(self, name: str) -> None:
        cp_obj: Optional[ClassProperty] = self.__get_classprop_attr(name)
        if cp_obj:
            cp_obj.__delete__(self)
        else:
            super(ClassPropertyMeta, self).__delattr__(name)
