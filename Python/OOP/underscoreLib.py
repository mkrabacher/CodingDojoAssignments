def multi2(x):
    return x * 2

class Underscore(object):
    def map(self, arr, func):
        for i in range(0, len(arr)):
            arr[i] = func(arr[i])
        return arr
    def reduce(self, arr, func):
        while len(arr) > 1:
            arr[0] = func(arr[0], arr[1])
            arr.pop(1)
        return arr
    def find(self, arr, func):
        for el in arr:
            if func(el):
                return el
    def filter(self, arr, func):
        newArr = []
        for el in arr:
            if func(el):
                newArr.append(el)
        return newArr
    def reject(self, arr, func):
        for el in arr:
            if func(el):
                arr.remove(el)
        return arr
        
_ = Underscore()

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print 'filter:', evens
evens = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)
print 'map:', evens
evens = _.reduce(range(0, 1000), lambda x,y: x + y)
print 'reduce:', evens
evens = _.find([1, 2, 4, 5, 6], lambda x: x % 3 == 0)
print 'find:', evens
evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)
print 'reject:', evens
