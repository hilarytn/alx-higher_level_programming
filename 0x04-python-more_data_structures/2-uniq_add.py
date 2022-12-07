#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    _sum = 0
    for x in new_list:
        _sum = _sum + x
    return _sum
