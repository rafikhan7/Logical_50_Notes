list_elements = [1, 2, 3, 4, 4, 6, 7, 9, 2, 4, 5]
def remove_duplicate(list_elements):
    result =[]
    for i in list_elements:
        if i not in result:
            result.append(i)
    return result

print(remove_duplicate(list_elements))
