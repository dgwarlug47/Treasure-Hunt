import random
from scipy.stats import bernoulli
from Components import Point
def wallGenerator(status):
    status.walls = []
    for xCoordinate in range(status.boardWidth):
        for yCoordinate in range(status.boardHeight):
            if (xCoordinate == 2 and yCoordinate == 2):
                continue
            coinFlip = bernoulli(status.wallProbability).rvs(1)[0]
            if (coinFlip == 1):
                alreadyThere = False
                for point in status.walls:
                    if (xCoordinate == point.x and yCoordinate == point.y):
                        alreadyThere = True
                        break
                if not alreadyThere:
                    status.walls.add(Point(xCoordinate, yCoordinate))

    if (len(status.walls) == status.boardWidth*status.boardHeight):
        wallGenerator(status)

import random
def choosePrizeLocation(status):
    xprize = None
    yprize = None

    while (True):
        xprize = random.choice(list(range(status.boardWidth)))
        yprize = random.choice(list(range(status.boardHeight)))
        if (xprize == 2 and yprize == 2):
            continue
        alreadyThere = False
        for point in status.walls:
            if (point.x == xprize and point.y == yprize):
                alreadyThere = True
                break
        if not alreadyThere:
            break
    
    status.xPrize = xprize
    status.yPrize = yprize

def isItInTheWalls(x, y, walls):
    isAlreadyThere = False
    for point in walls:
        if (x == point.x and y == point.y):
            isAlreadyThere = True
            break
    return isAlreadyThere