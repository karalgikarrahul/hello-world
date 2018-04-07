from math import sqrt
def is_prime(x):
    n = 2
    if x == n:
        return True
    y = int(sqrt(x))
    while y > n:
        if x%n != 0:
            n = n+1
            return True
        else:
            return False
def quadratic_primes():
    n = 0
    x = 0
    y = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            
