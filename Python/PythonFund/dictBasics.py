me = {'sex':'male', 'age':27, 'height':'6\'2"', 'name':'Matt', 'lang':'Klingon', 'birth_country':"'merica"}

def readMe(dict):
    for item in dict:
        # if item == 'lang':
        #     print 'My favorite language is {}'.format(dict['lang'])
        # elif item == 'name':
        #     print 'My name is {}'.format(dict['name'])
        # elif item == 'age':
        #     print 'My age is {}'.format(dict['age'])
        # elif item == 'height':
        #     print 'My height is {}'.format(dict['height'])
        # elif item == 'birth_country':
        #     print 'My country of birth is {}'.format(dict['birth_country'])
        # # elif item == 'sex':
        # #     print 'My gender is {}'.format(dict['sex'])
        # else:
        print 'My {} is {}'.format(item, dict[item])

readMe(me)