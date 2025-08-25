#Function to convert decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Example usage:
print(decimal_to_binary(10))  # Output: 1010