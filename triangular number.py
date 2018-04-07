i = 1
while i > 0:
    k = i
    i = i + 1
    sum = (k*(k+1))/2
    print sum
    count = 0
    for j in range(1, int(sum/2)):
        if sum%j == 0:
            count = count + 1
            if count == 500:
                i = 0
                print sum
                break
