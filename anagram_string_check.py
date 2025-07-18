def check_anagram(str1, str2):
    """Check if two strings are anagrams of each other."""
    #Remove spaces and convert to lowercase
    str1 =str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) ==sorted(str2)

string1 = "listen"
string2 = "silent"
output = check_anagram(string1, string2)
print(output)  # Output: True   