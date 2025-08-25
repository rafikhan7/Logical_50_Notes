#find te element of group of two number form list that totalis 9
#important Question
def find_group_of_elements_which_addition_9(lst, target=9):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                result.append((lst[i], lst[j]))
    return result

print(find_group_of_elements_which_addition_9([1, 2, 3, 4, 5, 6, 7, 8, 9]))