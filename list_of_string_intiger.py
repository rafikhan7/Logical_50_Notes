list_of_string_integers = ["1", "2", "3", "4", "5"]
def convert_to_string():
    result =[]
    for i in list_of_string_integers:
        result.append(int(i))
    return result

print(convert_to_string())
