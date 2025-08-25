#check_matching_character_in_two_string
str1 ="the holy grill"
str2 ="the lif is holy grail"
def check_matching_character_in_two_string(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)
    matching_characters = []
    for i in str1_list:
        if i in str2_list:
            matching_characters.append(i)
    return matching_characters

print(check_matching_character_in_two_string(str1, str2))

def check_matching_word_in_two_string(str1, str2):
    str1_list = str1.split()
    str2_list = str2.split()
    matching_words = []
    for i in str1_list:
        if i in str2_list:
            matching_words.append(i)
    return matching_words

print(check_matching_word_in_two_string(str1, str2))    