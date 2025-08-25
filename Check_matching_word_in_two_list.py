#Check_matching_word_in_two_list

from unittest import result


list_elem1 = ["apple", "banana", "cherry"]
list_elem2 = ["banana", "kiwi", "cherry"]
def check_list_matching(L1, L2):
    result=[]
    for i in L1:
        if i in L2:
            result.append(i)
    return result

print(check_list_matching(list_elem1, list_elem2))
