#!/usr/bin/python3

def str_cmp(s1, s2):
    pass

assert str_cmp('abc', 'Abc')
assert str_cmp('Hi there', 'hi there')
assert not str_cmp('foo', 'food')
assert str_cmp('nice', 'nice')
assert str_cmp('GoOd DaY', 'gOOd dAy')
assert not str_cmp('how', 'who')

print('all tests passed')
