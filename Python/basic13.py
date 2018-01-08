def oneTo255():
    for i in range(1,255):
        print i

def evensTo1000():
    for i in range(0, 501):
        print i * 2

def sum():
    sum = 0
    for i in range(0,256):
        sum += i
        return sum

arr = [0,1,2,3,-4,5,6,6,7]
def print_arr():
    '''
    hiasdf a
    '''
    for i in arr:
        print i

def print_max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def print_avg(arr):
    sum = 0.0
    for i in arr:
        sum += i
    return (sum / len(arr))

def odd_arr():
    arr = []
    for i in range(0,128):
        arr.append(1 + 2 * i)
    print arr

def sq_vals(arr):
    for i in range(0, len(arr)):
        arr[i] *= arr[i]
    print arr

def greater_y(arr, num):
    ct = 0
    for i in arr:
        if i > num:
            ct += 1
    print ct

def zero_out(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print arr
    return arr

def min_max_avg(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    
    print print_max(arr), print_avg(arr), min

def shift_array_values(arr):
    for i in range(len(arr) - 1, -1, -1):
        print i                                     #wrong
        arr[i] = arr[i-1]
    arr[0] = 0
    print arr

def dojo_out(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 'dojo'
    return arr

ta da