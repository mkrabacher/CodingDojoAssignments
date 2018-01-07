def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def isSquare(num):
    if num == 4 or num == 1:
        return True
    for i in range(1, (num / 2)):
        if i * i == num:
            return True
    return False

def fooBar():
    for num in range(100, 100000):
        if isPrime(num) and isSquare(num):
            print num, "Woah woah woah stop the beat a minute."
        elif isPrime(num):
            print num, "FOo"
        elif isSquare(num):
            print num, "Baarr"
        # else:
        #     print 'FooBarr'

fooBar()