#Capitalize first latter of string
def capitalize_char(string_data):
    if not string_data:
        return ""
    first_char = string_data[0]
    # Check if first_char is a lowercase letter
    if 'a' <= first_char <= 'z':
        # Convert to uppercase by subtracting 32 from ASCII value
        first_char = chr(ord(first_char) - 32)
    return first_char + string_data[1:]

# Example usage:
print(capitalize_char("hello world"))  # Output: Hello world