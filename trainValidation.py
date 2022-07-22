from curses import cbreak
import enum
from scipy.stats import bernoulli
from ActionManagement import ActionManagement, CheatReceiverActionManagement, StandardActionManagement
from Components import LearningStage, Point, ReceiverState, SenderAction, SenderState, Status, Movement
from QLearning import QTable
from Walls import wallGenerator, choosePrizeLocation, isItInTheWalls

def startNewEpisode(status):
    wallGenerator(status)
    choosePrizeLocation(status)

class Question(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4

question = Question.a
numberOfEpisodes = 100
senderInputSize = 5
terminationProbability = 1 - 0.95

receiverPossibleActions = [Movement.up, Movement.down, Movement.left, Movement.right]

recieverPossibleStates = []

for x in range(5):
    for y in range(5):
        for index in range(1, senderInputSize + 1):
            recieverPossibleStates.add(ReceiverState(x,y,str(index)))

senderPossibleActions = []

for index in range(1, senderInputSize + 1):
    senderPossibleActions.append(SenderAction(str(index)))


receiverQtable = QTable()
senderQtable = QTable()
sender = StandardActionManagement(senderQtable, list(range(1, senderInputSize + 1)))
if (question == Question.a):
    receiver = CheatReceiverActionManagement()
else:
    receiver = StandardActionManagement(receiverQtable, receiverPossibleActions)

status = Status(numberOfEpisodes)

for episode in range(status.numberOfEpisodes):
    startNewEpisode(status)
    senderState = SenderState(status.xPrize, status.yPrize)
    message = sender.choose(senderState)
    status.receiverX = 2
    status.receiverY = 2
    reward = None
    while(True):
        reward = None
        coinFlip = bernoulli(status.wallProbability).rvs(1)[0]
        if (coinFlip == 1):
            reward = 0
            break
        else:
            receiverState = ReceiverState(status.receiverX, status.receiverY, message)
            # choosing next action
            if (question != Question.a):
                direction = receiver.choose(receiverState, LearningStage.train)
            else:
                direction = receiver.choose(receiverState, senderState)

            desiredX = status.receiverX
            desiredY = status.receiverY
            if direction == Movement.up:
                desiredY = desiredY + 1
            if direction == Movement.down:
                desiredY = desiredY - 1
            if direction == Movement.left:
                desiredX = desiredX - 1
            if direction == Movement.right:
                desiredX = desiredX + 1
            
            if (desiredX < 0 or desiredX > 4 or desiredY < 0 or desiredY > 4):
                continue

            if (isItInTheWalls(status.receiverX)):
                continue

            status.currentX = desiredX
            status.currentY = desiredY

            if (status.currentX == status.xPrize and status.currentY == status.yPrize):
                reward = 1
                break

            
    
