
print 'X    1    2    3    4    5    6    7    8    9    10   11   12'
for row in range(1, 13):
    line = str(row)
    if len(str(row)) == 1:
        line += '    '
    if len(str(row)) == 2:
        line += '   '
    for col in range(1, 13):
        line += str((row) * (col))
        if len(str((row) * (col))) == 3:
            line += '  '
        elif len(str((row) * (col))) == 2:
            line += '   '
        elif len(str((row) * (col))) == 1:
            line += '    '
    print line