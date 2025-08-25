#count repeated character in a string

def check_repeated_characters(input_string):
    check_chractters={}
    for i in input_string:
        check_chractters[i] = check_chractters.get(i, 0) + 1
    return check_chractters

print(check_repeated_characters("Hello World"))