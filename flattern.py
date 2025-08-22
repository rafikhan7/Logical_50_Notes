
from unittest import result


data = [2,3,1,[48,38,20,[33,21,2]]]

def flatten(nested_list):
    result = []
    for x in nested_list:
        if (type(x) == list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

a = flatten(data)
print(a)