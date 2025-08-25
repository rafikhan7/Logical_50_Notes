#check given number list is ascending or not
list1=[1,2,3,4,5]
list2= [18,2,4,3,5,7,6]
def check_ascending(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

print(check_ascending(list1))
print(check_ascending(list2))