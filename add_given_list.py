#add given list

def add_given_list(input_list):
    """add given list elements."""
    result=0
    for i in range(len(input_list)):
        result += input_list[i]
    return result


print(add_given_list([1, 2, 3, 4, 5]))  # Output: 15