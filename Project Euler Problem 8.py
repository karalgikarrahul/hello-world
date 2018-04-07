z = int(raw_input("Enter a number: "))
r = 0
while z > 0:
    q = 1
    y = z % 10000000000000
    z = int(z/10)
    while y > 0:
        p = y%10
        y = int(y/10)
        q = p*q
    if q >= r:
        r = q
print r

