#Write a function divisible_by(numbers: list[int], divisor: int) that returns a generator.
#The generator should yield only the elements from numbers that are divisible by divisor.
#The function must use the yield keyword.

from typing import Iterable, Generator
def divisible_by(numbers: Iterable[int], divisor: int)->Generator[int, None, None]:
    for n in numbers:
        if n % divisor==0:
            yield n 
        
lst =[1,2,3,4,5,6,11,23,12]
print(list(divisible_by(lst, 3)))