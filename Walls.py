import random
from scipy.stats import bernoulli
from Components import Point, WallType
import random

def getMyWalls(status, computationalState):
    if status.wallType == WallType.fourRoom:
        fourRoomWallGenerator(computationalState)
    elif status.wallType == WallType.standard:
        standardWallGenerator(status, computationalState)
    elif status.wallType == WallType.empty:
        emptyWallGenerator(computationalState)
    

def standardWallGenerator(status, computationalState):
    computationalState.walls = []
    for xCoordinate in range(status.boardWidth):
        for yCoordinate in range(status.boardHeight):
            if (xCoordinate == 2 and yCoordinate == 2):
                continue
            coinFlip = bernoulli(status.wallProbability).rvs(1)[0]
            if (coinFlip == 1):
                alreadyThere = False
                for point in computationalState.walls:
                    if (xCoordinate == point.x and yCoordinate == point.y):
                        alreadyThere = True
                        break
                if not alreadyThere:
                    computationalState.walls.add(Point(xCoordinate, yCoordinate))

    if (len(computationalState.walls) == status.boardWidth*status.boardHeight - 1):
        standardWallGenerator(status, computationalState)

def emptyWallGenerator(computationalState):
    computationalState.walls = []

def fourRoomWallGenerator(computationState):
    computationState.walls = [
        Point(0,2),
        Point(1,2),
        Point(3,2),
        Point(4,2),
        Point(2,0),
        Point(2,4),
    ]

def choosePrizeLocation(computationState):
    xprize = None
    yprize = None

    while (True):
        xprize = random.choice(list(range(5)))
        yprize = random.choice(list(range(5)))
        if (xprize == 2 and yprize == 2):
            continue
        alreadyThere = False
        for point in computationState.walls:
            if (point.x == xprize and point.y == yprize):
                alreadyThere = True
                break
        if not alreadyThere:
            break
    
    computationState.xPrize = xprize
    computationState.yPrize = yprize

def isItInTheWalls(x, y, walls):
    isAlreadyThere = False
    for point in walls:
        if (x == point.x and y == point.y):
            isAlreadyThere = True
            break
    return isAlreadyThere