a = b = c = 0
while a < 1000:
    a += 1
    b = 1
    while b < 1000:
        b += 1
        c = 1
        while c < 1000:
            c += 1
            if a+b+c == 1000 and a*a + b*b == c*c:
                print a
                print b
                print c
                print a*b*c
                break
                
