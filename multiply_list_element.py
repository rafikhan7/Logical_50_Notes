#multiply list element

list_element =[1,2,3]

def multyply_list_element(list_element):
    total= 1
    for i in list_element:
        total =total*i
    return total

print(multyply_list_element(list_element))