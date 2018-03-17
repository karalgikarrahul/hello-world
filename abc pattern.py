list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
i = 0
n = 7
k = 1
z = 0
while n >= 0:
    while i < n:
        print list[i],
        i += 1
    print (z)*" ",
    i = 0
    while i < n:
        print list[-i-k],
        i = i + 1
    i = 0
    print "\n"
    n = n-1
    k = k + 1
    z = z + 4
    
