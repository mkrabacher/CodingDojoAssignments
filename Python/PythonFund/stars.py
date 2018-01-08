def draw_stars(nums):
    for i in nums:
        if type(i) == int:
            x = i
            tempS = ''
            while x > 0:
                x -= 1
                tempS += '*'
            print tempS
        elif type(i) == str:
            x = len(i)
            tempS = ''
            while x > 0:
                x -= 1
                tempS += i[0].lower()
            print tempS

draw_stars([4, 6, 1, 3, 5, 7, 25])
print '---------------------------------'
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])