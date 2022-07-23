from curses import cbreak
import enum
from scipy.stats import bernoulli
from ActionManagement import  CheatReceiverActionManagement, StandardActionManagement
from Components import LearningStage, Point, ReceiverState, SenderAction, SenderState, Status, Movement
from QLearning import QTable
from Walls import emptyWallGenerator, standardWallGenerator, choosePrizeLocation, isItInTheWalls
from UI import display_game

def startNewEpisode(status, question):
    if (question != Question.a):
        standardWallGenerator(status)
    else:
        emptyWallGenerator(status)
    choosePrizeLocation(status)

class Question(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4

question = Question.a
gridSizeX = 5
gridSizeY = 5
numberOfEpisodes = 5
earlyBreak = False

if (question == Question.a):
    senderInputSize = 1
else:
    senderInputSize = 5

terminationProbability = 1 - 0.95

receiverPossibleActions = [Movement.up, Movement.down, Movement.left, Movement.right]

recieverPossibleStates = []

for x in range(5):
    for y in range(5):
        for index in range(1, senderInputSize + 1):
            recieverPossibleStates.append(ReceiverState(x,y,str(index)))

senderPossibleActions = []

for index in range(1, senderInputSize + 1):
    senderPossibleActions.append(SenderAction(str(index)))

senderPossibleStates = []

for x in range(5):
    for y in range(5):
        senderPossibleStates.append(SenderState(x,y))


status = Status(numberOfEpisodes)

sender = StandardActionManagement(senderPossibleStates, senderPossibleActions, numberOfEpisodes)
if (question == Question.a):
    receiver = CheatReceiverActionManagement()
else:
    receiver = StandardActionManagement(recieverPossibleStates, receiverPossibleActions, numberOfEpisodes)

if (question == Question.a):
    status.wallProbability = 0
if (question != Question.a):
    status.wallProbability = 4/25
counter = 0
for currentEpisode in range(status.numberOfEpisodes):
    if (earlyBreak and counter > 5):
        break
    print("start new episode: " + str(currentEpisode))
    startNewEpisode(status, question)
    startSenderState = SenderState(status.xPrize, status.yPrize)
    senderAction = sender.choose(startSenderState, LearningStage.train)
    # TODO what if grid size changes
    status.receiverX = 2
    status.receiverY = 2
    reward = None
    while(True):
        display_game(gridSizeX, gridSizeY, status)
        counter += 1
        if (earlyBreak and counter > 5):
            break
        reward = None
        coinFlip = bernoulli(status.wallProbability).rvs(1)[0]
        if (coinFlip == 1):
            break

        startReceiverState = ReceiverState(status.receiverX, status.receiverY, senderAction)
        # choosing next action
        if (question != Question.a):
            receiverAction = receiver.choose(startReceiverState, LearningStage.train)
        else:
            receiverAction = receiver.choose(startReceiverState, startSenderState)

        desiredX = status.receiverX
        desiredY = status.receiverY
        if receiverAction.movement == Movement.up:
            desiredY = desiredY - 1
        if receiverAction.movement == Movement.down:
            desiredY = desiredY + 1
        if receiverAction.movement == Movement.left:
            desiredX = desiredX - 1
        if receiverAction.movement == Movement.right:
            desiredX = desiredX + 1
        print("direction", receiverAction.movement)

        print("desire", desiredX, desiredY)
        
        if (desiredX < 0 or desiredX > 4 or desiredY < 0 or desiredY > 4):
            reward=0
            pass

        elif (isItInTheWalls(desiredX, desiredY, status.walls)):
            reward=0
            pass
        else:
            reward=0
            status.receiverX = desiredX
            status.receiverY = desiredY

        foundPrize = False
        if (status.receiverX == status.xPrize and status.receiverY == status.yPrize):
            reward = 1
            foundPrize = True

        if (question != question.a):
            endReceiverState = ReceiverState(status.receiverX, status.receiverY, senderAction)
            receiver.updateQtable(
                startReceiverState, 
                receiverAction, 
                endReceiverState, 
                reward, 
                currentEpisode)

        if (foundPrize):
            break

    endSenderState = SenderState(0, 0,)

    sender.updateQtable(startSenderState, 
                senderAction, 
                endSenderState, 
                reward,
                currentEpisode)
    