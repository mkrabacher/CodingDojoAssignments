def oddEven():
    for i in range(0, 2000):
        state = ''
        if i % 2 == 0:
            state = 'even'
        else:
            state = 'odd'
        print 'Number is {}. This is an {} number.'.format(i, state)

# oddEven()

a = [2,4,10,16]

def multiply(list0, num):
    newList = []
    for i in list0:
        newList.append(i * num)
    return newList

# print multiply([2,4,5], 3)

def layered_multiples(arr):
    new_array = []
    for el in arr:
        tempArr = []
        x = el
        while x > 0:
            x -= 1
            tempArr.append(1)
        new_array.append(tempArr)

    return new_array


x = layered_multiples(multiply([2,4,5],3))
print x
