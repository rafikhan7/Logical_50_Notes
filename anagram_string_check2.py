#check two string is anagramor not
def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False    

anagram1 = input("Enter first string: ")    
anagram2 = input("Enter second string: ")
print(anagram(anagram1, anagram2))
