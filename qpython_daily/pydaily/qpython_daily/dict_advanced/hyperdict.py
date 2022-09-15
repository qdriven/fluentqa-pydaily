
from typing import Any, Optional, Union
import sys
import ast
import warnings
import copy

_UUID_EACH_FUNCTION = '64c7c93b7ecc4e09989ffbfef3e5 \
                      8d2fea7536f88d2e49f6b2917b14f8fc2603'
_UUID_POP_METHOD = 'f2f83f072c75445b9eb0e6dce2036e469 \
                      b24e1582165497881edd250baaccc44'


# ==================Helper classes==============================
class NoValue:
    '''
    No Value class.
    '''
    def __new__(cls, obj: Any = '<<|randome241#@-1215%string|>>') -> Any:
        if obj == '<<|randome241#@-1215%string|>>':
            return cls
        else:
            return obj


class NoKey:
    '''
    No Key class.
    '''
    def __new__(cls, obj: Any = '<<|randome241#@-1215%string|>>') -> Any:
        if obj == '<<|randome241#@-1215%string|>>':
            return cls
        else:
            return obj


class __EachHyperDictAssist:
    '''
    Helper class for each function.
    '''
    def __new__(cls):
        return _UUID_EACH_FUNCTION


def _keyerror(errors) -> None:
    errs = [i.args[0] for i in errors]
    msg = "Missing keys: "
    for i in errs:
        msg = msg + i + ', '
    msg = msg[:-2]
    warnings.warn(msg, Warning, stacklevel=3)


# ======================HyperDict Class=========================
class HyperDict:
    # Magic methods
    def __init__(self, dict_obj: Optional[dict] = None, **kw) -> None:
        if dict_obj is None:
            self.__hyper = {}
        else:
            self.__hyper = dict_obj
        self.__key_cache = {}
        self.k = list(self.__hyper.keys())
        self.v = list(self.__hyper.values())
        self.i = tuple(self.__hyper.items())
        try:
            self.no_val = kw['no_val']
        except Exception:
            self.no_val = '<<|randome241#@-1215%string|>>'
        try:
            self.no_key = kw['no_key']
        except Exception:
            self.no_key = '<<|randome241#@-1215%string|>>'

    def __getitem__(self, item: Union[tuple, int, str, bool]) -> Any:
        if type(item).__name__ == 'tuple':
            _values = list()
            for key in item:
                _values.append(self.__hyper.get(key, NoKey(self.no_key)))
            return tuple(_values)
        else:
            return self.__hyper.get(item, NoKey(self.no_key))

    def __setitem__(self, key: Union[tuple, int, str, bool],
                    value: Any) -> None:
        if type(key).__name__ in 'tuple':
            if (type(value).__name__ == 'list' and
                    value[-1] == _UUID_EACH_FUNCTION):
                value.pop()
                for neu, val in zip(key, value):
                    self.__hyper[neu] = val
            else:
                for neu in key:
                    self.__hyper[neu] = value
        else:
            self.__hyper[key] = value
        self.__update()

    def __delitem__(self, key: Union[tuple, int, str, bool]) -> None:
        __errors = []
        if type(key).__name__ in 'tuple':
            for i in key:
                try:
                    del self.__hyper[i]
                except KeyError as err:
                    __errors.append(err)
            if __errors != []:
                _keyerror(__errors)
        else:
            try:
                del self.__hyper[key]
            except KeyError as err:
                _keyerror([err])
        self.__update()

    def __repr__(self):
        return "HyperDict(" + str(self.__hyper) + ')'

    def __str__(self):
        return "HyperDict(" + str(self.__hyper) + ')'

    def __iter__(self):
        self.x = -1
        return self

    def __next__(self):
        neu = list(self.__hyper.keys())
        if self.x < len(neu) - 1:
            self.x += 1
            return list(self.__hyper.keys())[self.x]
        else:
            raise StopIteration

    def __hash__(self):
        return hash(str(self.__dict__))

    def __call__(self, *a):
        if a == ():
            return {i: self.__get_key(i) for i in self.v}

        try:
            trial = a[1]  # to check if list is singular or not
            del trial
            result = []
            for i in a:
                result.append(self.__get_key(i))
            return tuple(result)
        except IndexError:
            return self.__get_key(a[0])

    def __invert__(self):
        __lis = self.__hyper
        __result = {}
        for i, j in __lis.items():
            __result[j] = i
        return HyperDict(__result, no_val=self.no_key, no_key=self.no_val)

    def __pos__(self):
        return copy.deepcopy(self.__hyper)

    def __neg__(self):
        self.__hyper = {}
        self.__update()
        return self

    def __dict__(self):
        return self.__hyper

    def __contains__(self, key):
        return self.__hyper.__contains__(key)

    # Dicitionary methods
    def items(self):
        return self.__hyper.items()

    def keys(self):
        return self.__hyper.keys()

    def values(self):
        return self.__hyper.values()

    def clear(self):
        cl = self.__hyper.clear()
        self.__update()
        return cl

    def copy(self):
        return self.__hyper.copy()

    def fromkeys(self, seq, val=None):
        self.__hyper = self.__hyper.fromkeys(seq, val)
        return self.__hyper

    def get(self, key, val=None):
        return self.__hyper.get(key, val)

    def setdefault(self, key, val=None):
        return self.__hyper.setdefault(key, val)

    def popitem(self):
        return self.__hyper.popitem()

    def pop(self, key, default=_UUID_POP_METHOD):
        if _UUID_POP_METHOD == default:
            __p = self.__hyper.pop(key)
            self.__update()
            return __p
        else:
            __p = self.__hyper.pop(key, default)
            self.__update()
            return __p

    def update(self, dict=None, **kw):
        if dict is None:
            __d = self.__hyper.update()
            self.__update()
            return __d
        else:
            __d = self.__hyper.update(dict)
            self.__update()
            return __d

        if kw != {}:
            __d = self.__hyper.update(**kw)
            self.__update()
            return __d
        else:
            __d = self.__hyper.update()
            self.__update()
            return __d

    # HyperDict methods
    def hash(self):
        '''
        Returns hash for the dictionary exclusively.
        >>> d.hash() # Hash of the dictionary only.
        123...
        >>> hash(d) # Hash of the complete instance.
        321...

        '''
        return hash(str(self.__hyper))

    def change_no_value(self, obj):
        '''
        Change the default when an input value not found.
        '''
        self.no_val = obj

    def change_no_key(self, obj):
        '''
        Change the default when an input key not found.
        '''
        self.no_key = obj

    # Private methods
    def __get_key(self, value):
        try:
            if value in self.__key_cache:
                return self.__key_cache[value]
        except TypeError:
            ...
        keys = [i[0] for i in self.__hyper.items()]
        values = [i[1] for i in self.__hyper.items()]
        indices = []
        count = 0
        for i in values:
            if value == i:
                indices.append(count)
            count += 1

        if indices == []:
            return NoValue(self.no_val)
        else:
            try:
                result_tup = tuple([keys[i] for i in indices])
                self.__key_cache[value] = result_tup
                return self.__key_cache[value]
            except TypeError:
                return result_tup

    def __update(self):
        self.k = list(self.__hyper.keys())
        self.v = list(self.__hyper.values())
        self.i = tuple(self.__hyper.items())
        self.__clear_key_cache()

    def __clear_key_cache(self):
        self.__key_cache = {}


# ================FUNCTIONS====================================
def __argument_name(node):
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return node.attr
    elif (isinstance(node, ast.Subscript) and
          isinstance(node.slice, ast.Index) and
          isinstance(node.slice.value, ast.Str)):
        return node.slice.value.s
    elif isinstance(node, ast.Call):
        return node.func.id
    else:
        raise TypeError(f'Cannot extract name from {node}')


def to_hd(*args):
    '''
    Creates a dict with the same name as variable name.

    >>> name = 'Carlos'
    >>> age = 12
    >>> hd.to_hd(name, age)
    HyperDict({'name': 'Carlos', 'age': 12})
    '''
    try:
        import executing
    except ImportError:
        msg = """This function needs execution python package \
                Install using \npip install execution"""
        raise ImportError(msg)
    frame = sys._getframe(1)
    node = executing.Source.executing(frame).node
    return HyperDict({__argument_name(node): arg
                     for node, arg in zip(node.args, args)})


def each(*arr):
    '''
    Hyperdict assignment helper to assign
    multiple keys at the same time.

    >>> import hyperdict as hd
    >>> d = hd.HyperDict()
    >>> d['name', 'age'] = hd.each('Magnus', 31)
    >>> d
    HyperDict({'name': 'Magnus', 'age': 31})
    '''
    arr = list(arr)
    arr.append(__EachHyperDictAssist())
    return arr
