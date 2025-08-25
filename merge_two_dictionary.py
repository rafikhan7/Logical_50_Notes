#merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of dict1
    merged.update(dict2)    # Update with key-value pairs from dict2
    return merged

# Example usage:
dict_a = {"apple": 1, "banana": 2}
dict_b = {"banana": 3, "cherry": 4}
print(merge_dictionaries(dict_a, dict_b))