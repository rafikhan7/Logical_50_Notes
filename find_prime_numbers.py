#find prime numbers in a given range 0-100
def find_prime_numbers(start, end):
    """Find all prime numbers in a given range."""
    primes = [n for n in range(start, end+1 )if n>1 and  all(n%i !=0 for i in range(2, int(n**0.5) + 1))]
    return primes

print(find_prime_numbers(0, 100))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]