#map two list into a dictionary

name =["Alice", "Bob", "Charlie"]
age = [25, 30, 35]
def map_lists_to_dict(name, age):
    dict_person={}
    for i in range(len(name)):
        dict_person[name[i]]=age[i]
    return dict_person

print(map_lists_to_dict(name, age))