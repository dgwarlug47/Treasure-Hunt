def display_game(comp):
    walls = comp.walls
    xprize = comp.xPrize
    yprize = comp.yPrize
    currentX = comp.receiverX
    currentY = comp.receiverY
    ans = ''
    for y in range(5):
        for x in range(5):
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