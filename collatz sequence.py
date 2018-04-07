y = 0
x = 2
for x in range(9, 100):
    z = 0
    p = x
    while x > 1:
        if x%2 == 0:
            x = x/2
            z = z + 1
        else:
            x = 3*x + 1
            z = z + 1
    if z > y:
        y = z
print p
print y
