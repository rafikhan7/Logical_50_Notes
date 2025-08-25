#push all zero at the last of an list
from itertools import count


list_elm= [1,0,2,0,4,1,0,3,0,0,0,0,5,0,0]
def Push_all_zeros_to_end(lst):
    n= len(lst)
    count =0
    for i in range(n):
        if list_elm[i] !=0:
            list_elm[count]=list_elm[i]
            count += 1
    while count < n:
        list_elm[count]=0
        count += 1
    return list_elm

print(Push_all_zeros_to_end(list_elm))