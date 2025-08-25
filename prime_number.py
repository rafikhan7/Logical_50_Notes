prime_number = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
print(prime_number)