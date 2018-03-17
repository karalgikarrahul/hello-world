from math import sqrt
def is_prime(x):
    n = 2
    if x == n:
        return True
    while x > n:
        if x%n != 0:
            n = n+1
            return True
        else:
            return False
def largest_prime_factor(x):
    n = 2
    list = []
    while n <= x:
        if is_prime(n) == True and x%n == 0:
            x = x/n
            list.append(n)
            n = n+1
        else:
            n = n+1
    print list[-1]

largest_prime_factor(8095180192)
