#check anagram
import string


string1='listen'
string2='silent'
def check_anagram(string1, string2):
    if len(string1)!= len(string2):
        print("Not Anagrams")
    else:
        n =len(string1)
        for i in range(n):
            if string1[i] not in string2:
                return "Not Anagrams"
    return "Anagrams"
print(check_anagram(string1, string2))