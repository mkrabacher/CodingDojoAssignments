
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

arr = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

def filter(item):
    if isinstance(item, str):
        if len(item) >= 50:
            print "That a long string"
        else:
            print "Short strgin"
    elif isinstance(item, list):
        if len(item) >= 10:
            print 'long list'
        else:
            print 'short list'
    elif isinstance(item, int):
        if item >= 100:
            print 'big money'
        else:
            print 'small change'

for i in arr:
    filter(i)