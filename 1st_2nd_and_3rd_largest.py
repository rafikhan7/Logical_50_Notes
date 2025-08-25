# Find the 1st, 2nd, and 3rd largest numbers in a list
def find_largest_numbers(numbers):
   if not numbers or len(numbers)<3:
     print("List must contain at least three numbers.")
     return None, None, None
   first = second = third = float('-inf')
   for i in numbers:
        if i>first:
           third = second
           second=first
           first =i
        elif i >second:
           third = second
           second = i
        elif i > third:
           third = i

   return first, second, third

print(find_largest_numbers([1, 2, 3, 4, 5, 7, 10]))