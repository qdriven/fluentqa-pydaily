import hyperdict as hd
from hyperdict import HyperDict
import inspect

hd_1 = hd.HyperDict({'a': 1, 'b': 2, 'c': 3})
hd_2 = hd.HyperDict({'a': 'name',
                     1: 2,
                     (1, 2, 3): 2.1,
                     False: 1j,
                     'l': [2, 3, 1],
                     'h': {1: 0}})


# Overview
def test_version():
    assert hd.__version__ == '1.0.0'


def test_class():
    assert inspect.isclass(hd.HyperDict)


def test_instance():
    d = hd.HyperDict()
    assert isinstance(d, hd.HyperDict)


# Attributes
def test_i():
    assert hd_2.i == (('a', 'name'),
                      (1, 2),
                      ((1, 2, 3), 2.1),
                      (False, 1j),
                      ('l', [2, 3, 1]),
                      ('h', {1: 0}))


def test_k():
    assert hd_2.k == ['a', 1, (1, 2, 3), False, 'l', 'h']
    hd_2['test_k'] = 'test_v'
    assert hd_2.k == ['a', 1, (1, 2, 3), False, 'l', 'h', 'test_k']
    del hd_2['test_k']


def test_v():
    assert hd_2.v == ['name', 2, 2.1, 1j, [2, 3, 1], {1: 0}]
    hd_2['test_k'] = 'test_v'
    assert hd_2.v == ['name', 2, 2.1, 1j, [2, 3, 1],
                      {1: 0}, 'test_v']


def test_each():
    tes_d = hd.HyperDict()
    tes_d['name', 'age'] = hd.each('dimmy', 24)
    assert tes_d['name', 'age', 'random'] == ('dimmy', 24, hd.NoKey)
    del tes_d


def test_to_hd():
    language = 'Python'
    year = 1991
    founded = 'Guido'
    d = hd.to_hd(language, year, founded)
    assert str(d) == str(HyperDict({'language': 'Python',
                                    'year': 1991, 'founded': 'Guido'}))


# Methods
def test_init():
    a = hd.HyperDict()
    assert a.k == []
    assert a.i == ()
    assert a.v == []
    assert a.no_val == '<<|randome241#@-1215%string|>>'
    assert a.no_key == '<<|randome241#@-1215%string|>>'


def test_getter():
    assert hd_1['a', 'b'] == (1, 2)
    assert hd_1['c'] == 3


def test_setter():
    hd_1['d', 'e'] = hd.each(4, 5)
    assert hd_1['a', 'd', 'e'] == (1, 4, 5)


def test_deleter():
    del hd_1['e']
    assert hd_1['a', 'e'] == (1, hd.NoKey)


def test_repr():
    assert str(hd_1) == str(HyperDict({'a': 1, 'b': 2, 'c': 3, 'd': 4}))


def test_iter():
    for i, j in zip(hd_1, hd_1.v):
        assert hd_1[i] == j


def test_hash():
    assert type(hash(hd_2)).__name__ == 'int'


def test_call():
    assert hd_1(1, 2) == (('a', ), ('b', ))
    assert hd_1(3) == (('c', ))
    hd_1['f'] = 3
    assert hd_1() == {1: ('a',), 2: ('b',), 3: ('c', 'f'), 4: ('d',)}


def test_inv():
    assert str(~hd_1) == str(HyperDict({1: 'a', 2: 'b', 3: 'f', 4: 'd'}))


def test_pos():
    assert +hd_1 == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 3}


def test_neg():
    assert str(-hd_1) == str(HyperDict({}))


def test_dict():
    assert dict(hd_1) == {}


hd_1 = hd.HyperDict({'a': 1, 'b': 2, 'c': 3})


def test_in():
    hd_1 = hd.HyperDict({'a': 1, 'b': 2, 'c': 3})
    a = 'a' in hd_1
    assert a


def test_items():
    assert list(hd_2.items()) == [('a', 'name'),
                                  (1, 2),
                                  ((1, 2, 3), 2.1),
                                  (False, 1j),
                                  ('l', [2, 3, 1]),
                                  ('h', {1: 0}),
                                  ('test_k', 'test_v')]


def test_keys():
    assert list(hd_2.keys()) == ['a', 1, (1, 2, 3), False, 'l', 'h', 'test_k']


def test_values():
    assert list(hd_2.values()) == ['name', 2, 2.1, 1j, [2, 3, 1], {1: 0},
                                   'test_v']


def test_clear():
    assert hd_1.clear() is None


def test_copy():
    hd_1 = hd.HyperDict({'a': 1, 'b': 2, 'c': 3})
    assert str(hd_1.copy()) == "{'a': 1, 'b': 2, 'c': 3}"


def test_fromkeys():
    hd_3 = hd.HyperDict()
    hd_3.fromkeys([1, 2, 3], None)
    assert str(hd_3) == str(HyperDict({1: None, 2: None, 3: None}))


def test_get():
    assert hd_2.get((1, 2, 3), None) == 2.1
    assert hd_2.get((1, ), "No!") == "No!"


def test_setdefault():
    assert hd_2.setdefault('l', 'No!') == [2, 3, 1]
    assert hd_2.setdefault('g', 'No!') == 'No!'


def test_popitem():
    hd_3 = hd.HyperDict({1: 31, 2: 13, 4: 'a'})
    assert hd_3.popitem() == (4, 'a')


def test_pop():
    hd_3 = hd.HyperDict({1: 31, 2: 13, 4: 'a'})
    assert hd_3.pop(1) == 31


def test_update():
    hd_3 = hd.HyperDict({1: 31, 2: 13, 4: 'a'})
    hd_3.update({100: 100})
    assert hd_3.popitem() == (100, 100)


def test_meth_hash():
    assert type(hd_2.hash()).__name__ == "int"


def test_change_no_key():
    hd_3 = hd.HyperDict({1: 31, 2: 13, 4: 'a'})
    hd_3.change_no_key('No!')
    assert hd_3[3] == 'No!'
    assert hd_3[1, 5] == (31, 'No!')


def test_change_no_value():
    hd_3 = hd.HyperDict({1: 31, 2: 13, 4: 'a'})
    hd_3.change_no_value('No!')
    assert hd_3('b') == 'No!'
    assert hd_3(31, 'a', 'c') == ((1, ), (4, ), 'No!')
