#Write a function to convert binary number to decimal
def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal
print(binary_to_decimal("101010"))  # Output: 10