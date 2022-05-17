#!/usr/bin/env python
# -*- coding:utf-8 -*-
import inspect
from threading import Lock
from typing import TypeVar, Optional, Generic, Dict, Callable, Any, Union, List, Tuple, FrozenSet

T = TypeVar("T", bound="SingletonMeta")


class SingletonMeta(type, Generic[T]):
    """
    Simple Singleton in Python
    """
    _instance: Optional[T] = None

    def __call__(cls: T, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonMeta, cls).__calll__(*args, **kwargs)

        return cls._instance


class ThreadSafeMixin(type):
    def __init__(cls, name: str, bases: tuple, dct: dict):
        super(ThreadSafeMixin, cls).__init__(name, bases, dct)
        # add a lock for thread safety
        cls._lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # use the lock
        with cls._lock:
            return super(ThreadSafeMixin, cls).__call__(*args, **kwargs)


G = TypeVar("G", bound="SingletonArgsMeta")


class SingletonArgsMeta(type, Generic[G]):
    """
    Singleton that keep single instance for single set of arguments.
    """
    _instances: Dict[int, G] = {}
    _init: Dict[G, Callable] = {}

    def __init__(cls: G, name: str, bases: tuple, dct: dict) -> None:
        super(SingletonArgsMeta, cls).__init__(name, bases, dct)

        # save the __init__ method of each class that uses this singleton
        # required in __call__ method below
        cls._init[cls] = getattr(cls, "__init__")

    def __call__(cls: G, *args, **kwargs) -> T:
        # get the individual calling signature of the __init__ method for this class
        init_callargs: Dict[str, Any] = \
            inspect.getcallargs(cls._init[cls], None, *args, **kwargs)

        # create a key
        key: int = hash(
            # the individual key is this class combined with the signature above
            (cls, cls.__freeze(init_callargs))
        )

        # check if there's already an instance that has the same __init__ signature
        if key not in cls._instances:
            # if not, create it
            cls._instances[key] = super(SingletonArgsMeta, cls).__call__(*args, **kwargs)

        return cls._instances[key]

    def __freeze(cls, set_obj: Union[Dict[Any, Any],
                                     List[Any], Tuple[Any]]) \
            -> Union[FrozenSet[Any], Tuple[Any], Any]:
        """
        Recursively transform a dictionary to a frozenset. This can be hashed.
        @param set_obj: The dictionary that should be converted.
        @return: A frozenset from the above dictionary.
        """
        if isinstance(set_obj, dict):
            return frozenset((key, cls.__freeze(value)) for key, value in set_obj.items())
        elif isinstance(set_obj, list):
            return tuple(cls.__freeze(value) for value in set_obj)
        return set_obj
