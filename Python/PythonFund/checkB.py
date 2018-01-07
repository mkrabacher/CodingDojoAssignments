black = False
for line in range(0, 8):
    row = ''
    black = not black
    for sq in range(0, 8):
        if black:
            row += '*'
            black = False
        else:
            row += ' '
            black = True
    print row