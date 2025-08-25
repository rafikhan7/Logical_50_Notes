#swap_list_elemnts i = 1, j = 3 
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_swap_element(list_elements, i=1, j=3):
    list_elements[i], list_elements[j] = list_elements[j], list_elements[i]
    return list_elements

print(list_swap_element(list_elements))