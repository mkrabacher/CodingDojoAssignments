import random

def coinToss(times):
    heads = 0
    tails = 0
    for flip in range(0, times):
        x = round(random.random())
        if x == 1:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's heads! ... Got {} head(s) so far and {} tail(s) so far".format(flip + 1, heads, tails)
        elif x == 0:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's tails! ... Got {} head(s) so far and {} tail(s) so far".format(flip + 1, heads, tails)

coinToss(5000)