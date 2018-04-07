import random
print "Keep a number in your mind"
x = raw_input("press 'y' when ready: ")
if x == 'y':
    print "Multiply your number by 2"
x = raw_input("press 'y' when ready: ")
if x == 'y':
    z = random.randint(1, 100)
    if z%2 == 0:
        print "Add %d to your present value and divide that by 2. " % (z)
        print "After this subtract current value with original number"
        z = z/2
        p = raw_input("Enter 'M' to know your number: ")
        if p == 'M':
            print "Your current number is %d" % (z)
        else:
            print "try again"
    else:
        z = z+1
        print "Add %d to your present value and divide that by 2. " % (z)
        print "After this subtract current value with original number"
        z = z/2
        p = raw_input("Enter 'M' to know your number: ")
        if p == 'M':
            print "Your current number is %d" % (z)
        else:
            print "try again"
