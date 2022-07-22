import enum
from shutil import move
import json


class Movement(enum.Enum):
    up = 1
    down = 2
    left = 3
    right = 4

class State():
    def __init__(self) -> None:
        pass

class SenderState(State):
    def __init__(self, xprize, yprize) -> None:
        self.xprize = xprize
        self.yprize = yprize

        self.id = "sender id: xprize: " + str(xprize) + ", yprize:" + str(yprize) 

class ReceiverState(State):
    def __init__(self, currentX, currentY, message) -> None:
        self.currentX = currentX
        self.currentY = currentY
        self.message = message

        self.id = "receiver id: x:" + str(self.currentX) + ", y:" + str(self.currentY) + ", message: " + str(self.message)

class Action():
    def __init__(self) -> None:
        pass

class SenderAction(Action):
    def __init__(self, message) -> None:
        self.message = message
        self.id = message

class ReceiverAction(Action):
    def __init__(self, movement) -> None:
        self.movement = movement
        if movement == Movement.up:
            self.id = "up"
        if movement == Movement.down:
            self.id = "down"
        if movement == Movement.left:
            self.id = "left"
        if movement == Movement.right:
            self.id = "right"

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Status():
    def __init__(self, numberOfEpisodes) -> None:
        self.numberOfEpisodes = numberOfEpisodes
        self.boardWidth = 5
        self.boardHeight = 5
        self.wallProbability = None
        self.xPrize = None
        self.yPrize =  None
        self.walls = []

        self.receiverX = None
        self.receiverY = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent='\n')


    def __repr__(self) -> str:
        return json.dumps(self.toJSON())


class LearningStage(enum.Enum):
    train = 1
    test = 2