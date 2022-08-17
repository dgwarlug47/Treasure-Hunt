from scipy.stats import bernoulli
from actionManagement import StandardActionManagement
from components import ComputationState, LearningStage, ReceiverAction, ReceiverState, RewardsInEpisode, SenderAction, SenderState, Settings, Movement
from Walls import getMyWalls, choosePrizeLocation, isItInTheWalls
from gridUI import display_game
import time
def startNewEpisode(status, computationalState):
    getMyWalls(status, computationalState)
    choosePrizeLocation(computationalState)

def trainAndTest(trainStatus, testStatus):
    sender, receiver= train(trainStatus)

    test(testStatus, sender, receiver)

def train(status, testNum):
    earlyBreak = False
    receiverPossibleActions = [ReceiverAction(Movement.up), 
                                ReceiverAction(Movement.down), 
                                ReceiverAction(Movement.left), 
                                ReceiverAction(Movement.right)]
    receiverPossibleStates = []

    for x in range(5):
        for y in range(5):
            for index in range(1, status.senderInputSize + 1):
                receiverPossibleStates.append(ReceiverState(x,y,str(index)))

    senderPossibleActions = []
    for index in range(1, status.senderInputSize + 1):
        senderPossibleActions.append(SenderAction(str(index)))

    senderPossibleStates = []
    for x in range(5):
        for y in range(5):
            senderPossibleStates.append(SenderState(x,y))

    sender = StandardActionManagement(senderPossibleStates, 
                                senderPossibleActions, 
                                status.numberOfEpisodes,
                                status.epsilon)

    receiver = StandardActionManagement(receiverPossibleStates, 
                                        receiverPossibleActions, 
                                        status.numberOfEpisodes,
                                        status.epsilon)


    sender, _, receiver, _= run(status, earlyBreak,
            sender,
            receiver,
            LearningStage.train,
            testNum)

    return sender, receiver

def test(status,
            sender, 
            receiver,
            testNum):
        
    _, senderRewards, _, receiverRewards = run(status, False, sender, receiver,
            LearningStage.test, testNum)

    return senderRewards, receiverRewards


def run(status, 
        earlyBreak, 
        sender, 
        receiver, 
        learningStage,
        testNum):
    
    computationState = ComputationState()
    counter = 0
    receiverRewards = []
    senderRewards = []
    startSenderState = None
    senderAction = None
    senderReward = None
    tim=None
    for currentEpisode in range(status.numberOfEpisodes):
        inEpisodeSenderRewards = RewardsInEpisode()
        inEpisodeReceiverRewards = RewardsInEpisode()
        if (earlyBreak and counter > 5):
            break
        if (currentEpisode % 200 == 0):
            lastTime = tim
            tim = time.time()
            if (lastTime != None):
                print("time, ", str(tim - lastTime))
            print("numberOfEpisodes" + str(status.numberOfEpisodes))
            print("epsilon" + str(status.epsilon))
            print("senderInputSize" + str(status.senderInputSize))
            print("episode" + str(currentEpisode))
            print("numTest" + str(testNum))
        startNewEpisode(status, computationState)
        prevSenderState = startSenderState
        startSenderState = SenderState(computationState.xPrize, 
                        computationState.yPrize)
        
        prevSenderAction = senderAction
        if learningStage == LearningStage.train and prevSenderState != None:
            sender.updateQtable(prevSenderState, 
                        prevSenderAction, 
                        startSenderState, 
                        senderReward,
                        currentEpisode)
        
        senderAction = sender.choose(startSenderState, learningStage)
        computationState.receiverX = 2
        computationState.receiverY = 2
        receiveReward = None
        senderReward = None

        while(True):            
            # display_game(computationState)
            counter += 1
            if (earlyBreak and counter > 5):
                break
            coinFlip = bernoulli(status.terminationProbability).rvs(1)[0]
            if (coinFlip == 1):
                senderReward = 0
                break

            startReceiverState = ReceiverState(computationState.receiverX, computationState.receiverY, senderAction.message)
            # choosing next action
            receiverAction = receiver.choose(startReceiverState, learningStage)

            desiredX = computationState.receiverX
            desiredY = computationState.receiverY
            if receiverAction.movement == Movement.up:
                desiredY = desiredY - 1
            if receiverAction.movement == Movement.down:
                desiredY = desiredY + 1
            if receiverAction.movement == Movement.left:
                desiredX = desiredX - 1
            if receiverAction.movement == Movement.right:
                desiredX = desiredX + 1
            
            if (desiredX < 0 or desiredX > 4 or desiredY < 0 or desiredY > 4):
                receiveReward = 0
                pass

            elif (isItInTheWalls(desiredX, desiredY, computationState.walls)):
                receiveReward = 0
                pass
            else:
                receiveReward = 0
                computationState.receiverX = desiredX
                computationState.receiverY = desiredY

            foundPrize = False
            if (computationState.receiverX == computationState.xPrize and computationState.receiverY == computationState.yPrize):
                receiveReward = 1
                foundPrize = True

            endReceiverState = ReceiverState(computationState.receiverX, computationState.receiverY, senderAction.message)

            inEpisodeReceiverRewards.add(receiveReward)

            if learningStage == LearningStage.train:
                receiver.updateQtable(
                    startReceiverState, 
                    receiverAction, 
                    endReceiverState, 
                    receiveReward, 
                    currentEpisode)

            if (foundPrize):
                senderReward = 1
                break

        inEpisodeSenderRewards.add(senderReward)
        
        senderRewards.append(inEpisodeSenderRewards)
        receiverRewards.append(inEpisodeReceiverRewards)
    return sender, senderRewards, receiver, receiverRewards