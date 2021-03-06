#!/usr/bin/env python

from pyrefine import *


def gcd2(x, y):
    define_('int -> int -> int',
            'x > 0 and y > 0',
            'ret > 0')
    t = c_('int', 0)
    while x != y:
        loop_('x > 0 and y > 0', 'x + y')
        if x > y:
            y, x = x, y
        assert y > x
        y = y - x
    assert x == y
    return y


def simple(x, y):
    define_('int -> int -> int',
            'x > 0 and y > 0',
            'ret == x + y')
    a = c_('int', x)
    res = c_('int', 0)
    res = a + y
    return res


def simple_if(x, y):
    define_('int -> int -> int',
            'x != 0',
            'ret > 0')
    a = c_('int', 0)
    a = x
    if x < 0:
        a = -x
    return a


def simple_if2(x, y):
    define_('int -> int -> int',
            'y >= 0 and x >= 0',
            'ret > 0')
    a = c_('int', 1)
    if y > x:
        a = y
    b = c_('int', y)
    return a + b


def simple_if3(x, y):
    define_('int -> int -> bool',
            'y >= 0',
            'ret == True')
    if x > y:
        x = y
    return x <= y


def simple_if_else(x, y):
    define_('int -> int -> int',
            'True',
            'ret > 0')
    a = c_('int', 0)
    if x > y:
        a = x - y
    else:
        a = y - x + 1
    return a


def simple_while(x):
    define_('int ->  int',
            'x > 0',
            'ret > 0')
    s = c_('int', x)
    x = x - 1
    while x != 0:
        loop_('x >= 0 and s > 0', 'x')
        s = s + x
        x = x - 1
    return s


def simple_while2(x):
    define_('int ->  int',
            'x >= 0',
            'ret >= 0')
    s = c_('int', 0)
    i = c_('int', 0)
    while i != x:
        loop_('0 <= s and x >= 0 and 0 <= i <= x ', 'x - i')
        s = s + i
        i = i + 1
    return s


def gcd(x, y):
    define_('int -> int -> int',
            'x > 0 and y > 0',
            'ret > 0')
    while x != y:
        loop_('x > 0 and y > 0', 'x + y')
        if x < y:
            y = y - x
        else:
            x = x - y
    return y


def proof():
    define_('int', 'True', 'True')
    implies = define_('bool -> bool -> bool', 'True',
                 'ret == (a >> b)',
                 lambda a, b: b if a else True)
    # (a /\ b) -> a
    prop1 = define_('bool -> bool -> bool', 'True', 'ret',
                 lambda a, b: implies((a and b), a))
    # a -> ((a -> b) -> b)
    prop2 = define_('bool -> bool -> bool', 'True', 'ret',
                 lambda a, b: implies(a, implies(implies(a, b), b)))
    # a \/ ~a
    excluded_middle = define_('bool -> bool', 'True', 'ret',
                 lambda a: a or not a)
    # ~(a /\ b) <-> ~a \/ ~b
    de_morgan = define_('bool -> bool -> bool', 'True', 'ret',
                 lambda a, b: not (a and b) == (not a or not b))

    assert implies(False, False)
    assert implies(False, True)
    assert not implies(True, False)
    assert implies(True, True)


if __name__ == '__main__':
    print(gcd(8, 12))
    proof()

    print("Done")
