# Sort a list of dictionaries by a specific key
list_of_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

sorted_list = sort_by_key(list_of_dicts, "age")

print(sorted_list)