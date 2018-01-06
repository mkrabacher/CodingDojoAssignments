words = "It's thanksgiving day. It's my birthday,too!"

print words
print words.index('day')
words2 = words.replace('day', 'month', 1)
print words2

x = ["hello",2,54,-2,7,12,98,"world"]

print x[len(x) - 1]

print x[:1]

arr = x[:1]

arr.append(x[len(x) - 1])

print arr

x = [19,2,54,-2,7,12,98,32,10,-3,6]

print x

x.sort()

print x

y = x[len(x)/2 - 1:]

print y

y[0] = x[:len(x)/2]

print y