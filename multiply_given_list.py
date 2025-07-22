#multiply all numbers in a given list

def multiply_given_list(input_list):
    """Multiply all numbers in a given list."""
    result = 1
    for i in range(len(input_list)):
        result *= input_list[i]
    return result

list_elements = [1, 2, 3, 4, 5]
print(multiply_given_list(list_elements))  # Output: 120