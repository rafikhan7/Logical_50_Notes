#add all list elements
from re import I
import re


list_elements = [1, 2,3,4,5,6,7,8,9]
def add_list_elements(list_elements):
    for i in list_elements:
        sums = 0
        sums = sums + i

    return sums

print(add_list_elements(list_elements))