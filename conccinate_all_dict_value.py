#write a program to conccinate all dict value in single string
import string


dict_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "occupation": "Engineer",
    "hobby": "Reading",
    "favorite_color": "Blue",
    "pet": "Cat",
    "other": "None"
}
def concatenate_dict_values(data):
    string=" "
    for key, value in dict_data.items():
        string += str(value) + " "
    return string.strip()

print(concatenate_dict_values(dict_data))
