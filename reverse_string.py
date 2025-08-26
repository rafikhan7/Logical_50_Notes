#create a function that takes a string as input and returns the string reversed
def reverse_string(s):
    reverse_string=""
    for char in s:
        reverse_string = char + reverse_string
    return reverse_string

print(reverse_string("Hello"))  # Output: "olleH"