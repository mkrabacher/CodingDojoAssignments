l = ['magical unicorns',19,'hello',98.98,'world']

a = [2,3,1,7,4,12]

b = ['magical','unicorns']

tests = [l, a, b]

def typeCheck(list):
    nums = False
    strs = False
    types = 0
    conStr = ''
    numSum = 0
    for item in list:
        if isinstance(item, str):
            strs = True
            conStr += ' ' + item
            
        elif isinstance(item, int) or isinstance(item, float):
            nums = True
            numSum += item

    if nums and strs:
        print 'the list you entered is a mixed list'
        print 'String: ' + conStr
        print 'sum: ' + str(numSum)
    elif strs:
        print 'the list you entered is of string types'
        print 'String: ' + conStr
    elif nums:
        print 'the list you entered is of string types'
        print 'sum: ' + str(numSum)

    
for i in tests:
    print '--------------------------------------------'
    typeCheck(i)
    print '--------------------------------------------'