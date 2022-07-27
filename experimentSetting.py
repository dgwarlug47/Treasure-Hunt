from tkinter.messagebox import QUESTION
from components import Question, Settings, WallType

def getTrainTestStatus(Nep, epsilon, senderInputSize, wallType):
    trainStatus = Settings()
    trainStatus.numberOfEpisodes = Nep
    trainStatus.epsilon = epsilon
    trainStatus.terminationProbability = 1 - 0.95
    trainStatus.senderInputSize = senderInputSize
    trainStatus.wallProbability = -10
    trainStatus.wallType = wallType

    testStatus = Settings()
    testStatus.numberOfEpisodes = 1000
    testStatus.terminationProbability = 1 - 0.95
    testStatus.epsilon = 0
    testStatus.senderInputSize = senderInputSize
    testStatus.wallProbability = -10
    testStatus.wallType = wallType

    return trainStatus, testStatus