list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

one = [1,2,5,6,5]
two = [1,2,5,6,5,3]

list_o = [1,2,5,6,5,16]
list_t = [1,2,5,6,5]

list_1 = ['celery','carrots','bread','milk']
list_2 = ['celery','carrots','bread','cream']

def comp(listA, listB):
    if listA == listB:
        return 'The lists are the same'
    else:
        return 'The lists are not the same'


print comp(list_1, list_2)