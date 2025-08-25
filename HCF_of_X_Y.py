# Function to calculate HCF of two numbers
def check_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if (x%i==0) and(y%i==0):
            hcf=i
    return hcf

print(check_hcf(54, 24))
