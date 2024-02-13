def checkPrimeNumber(n):
    if n <= 3: 
        return n > 1 # if n is either 2 or 3, it return true
    if n % 2 == 0 or n % 3 == 0: # if n is even, and diviable for 3, return false
        return False
    # the loop starts from 5, this will be 6k - 1. We check all the number 
    # that 6k + 1 > sqrt(n) or 6k - 1 > sqrt(n)
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def getPrimeNumbers(n):
    return [i for i in range(2, n) if checkPrimeNumber(i)]

print(getPrimeNumbers(20))