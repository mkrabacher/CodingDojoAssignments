screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

def fill(y,x,oldColor,newColor,screen):
    if y < 0 or x < 0 or y >= len(screen) or x >= len(screen[0]):
        return
    if screen[y][x] != oldColor:
        return
    
    screen[y][x] = newColor

    if screen[y-1][x] == oldColor:
        fill(y-1,x,oldColor,newColor,screen)
    if screen[y+1][x] == oldColor:
        fill(y+1,x,oldColor,newColor,screen)
    if screen[y][x-1] == oldColor:
        fill(y,x-1,oldColor,newColor,screen)
    if screen[y][x+1] == oldColor:
        fill(y,x+1,oldColor,newColor,screen)


    return screen

print '='*20
print fill(4,4,2,3,screen)
print '*'*20