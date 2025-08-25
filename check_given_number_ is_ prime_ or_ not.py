#check given number is prime or not
def check_prime(num):
    if num> 1:
        for  i in range(2, num):
            if(num%i)==0:
                return False
        return True
    return False

print(check_prime(11))