#merge two list
x=[1,3,5,7,9]
y=[2,4,6,8,10]
#reverse the list
print(y[::-1])
def merge_two_list(x,y):
    y.extend(x)
    return y

print(merge_two_list(x,y))