#write a program  function to convert string of all character in upercase without using upper()
def to_uppercase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Example usage
input_str = "Hello World!"
result = to_uppercase(input_str)
print(result)
