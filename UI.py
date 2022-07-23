from Components import Point

def display_game(grid_sizex, grid_sizey, status):
    walls = status.walls
    xprize = status.xPrize
    yprize = status.yPrize
    currentX = status.receiverX
    currentY = status.receiverY
    ans = ''
    for y in range(grid_sizey):
        for x in range(grid_sizex):
            newChar = '~'
            if (x==currentX and y ==currentY):
                newChar = 'J'
            if (x==xprize and y==yprize):
                newChar = 'P'
            for point in walls:
                if (point.x == x and point.y == y):
                    newChar = 'W'
                    break
            ans += newChar
            ans += '|'
        ans += '\n'
    print(ans)
    return ans
            
            

def validation(walls, xprize, yprize, currentX, currentY):
    assert(xprize != currentX or yprize != currentY)
    for point in walls:
        assert(point.x != xprize or point.y != yprize)
        assert(point.x != currentX or point.y != currentY)

# ans = display_game(4,4,[Point(0,0), Point(1,1)], 2,3,1,2)