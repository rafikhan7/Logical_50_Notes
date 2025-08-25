#check_list_elem_frequency
list_elements = [1, 2, 3, 2, 1, 2, 3, 1, 0, 4, 5, 6, 6, 7, 7, 8, 9]
def check_frequency(lst):
    frequency={}
    for item in lst:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency

print(check_frequency(list_elements))