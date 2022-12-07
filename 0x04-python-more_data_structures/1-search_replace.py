#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    for x in range(len(my_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
"""
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
newlist = search_replace(my_list, 2, 89)

print(newlist)
print(my_list)"""
