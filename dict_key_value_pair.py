#make dict_key value pair
dict= {1:1, 2:2,3:3, 4:4, 5:5}

def make_dict_key_value_pair(dict):
    pair =()
    for k,v in  dict.items():
        pair += ((k,v),)
    return pair

print(make_dict_key_value_pair(dict))