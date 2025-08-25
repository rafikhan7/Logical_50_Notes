# Function to check if a number is a palindrome
from unicodedata import digit

def check_palindrome(nume):
    temp =nume
    revers =0
    while(nume>0):
        digit = nume % 10
        revers = (revers * 10) + digit
        nume //= 10
    if temp == revers:
        return True
    return False
