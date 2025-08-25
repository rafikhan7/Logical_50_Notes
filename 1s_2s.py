#sort 0s, 1s, 2s
arr = [0, 1, 2, 3, 4, 5, 6, 1, 0, 0, 1, 3, 2, 0, 1]

def sort012(arr):
    Low=0
    Mid= 0
    High=len(arr)-1
    while Mid<=High:
        if arr[Mid]==0:
            arr[Low], arr[Mid] = arr[Mid], arr[Low]
            Low += 1
            Mid += 1
        elif arr[Mid]==1:
            Mid += 1
        else:
            arr[Mid], arr[High] = arr[High], arr[Mid]
            High -= 1
    return arr

sort_array=sort012(arr)
print(sort_array)