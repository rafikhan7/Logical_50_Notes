#sort_list_without_inbuilt_method
list_elements = [5, 2, 9, 1, 5, 6]

def sort_list(list_elements):
    n = len(list_elements)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_elements[j] > list_elements[j+1]:
                list_elements[j], list_elements[j+1] = list_elements[j+1], list_elements[j]
    return list_elements

print(sort_list(list_elements))