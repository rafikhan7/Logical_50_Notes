#find missing value from list sequenc
list_element = [1,3,4,5,6]
def find_missing_element_from_list(lst):
    n =len(lst)
    for i in range(1, n+2):
        if i not in lst:
            return i

print(find_missing_element_from_list(list_element))