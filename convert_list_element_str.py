# convert list elements into str

def convert_list_element_str(input_list):
    new_elements_str=[]
    for i in range(len(input_list)):
        new_elements_str.append(str(i))
    return new_elements_str

print(convert_list_element_str([1, 2, 3, 4, 5]))