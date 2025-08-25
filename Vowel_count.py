#create a function to find Vowel count with unique string
def unique_vowel_count(input_string):
    vowel="aeiouAEIOU"
    unique_vowel_count=set()
    for char in input_string:
        if char in vowel:
            unique_vowel_count.add(char.lower())
    return unique_vowel_count

print(unique_vowel_count("Hello World"))