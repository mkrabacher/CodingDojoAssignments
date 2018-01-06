#Multiples
#part 1
for num in range(0, 1000):
    if num % 2 != 0:
        print num

#part 2
for num in range(0, 1000000):
    if num % 5 == 0:
        print num

#sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum += num
print sum

#average list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum += num
print sum/len(a)