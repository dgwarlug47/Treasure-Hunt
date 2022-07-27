from Components import Settings, WallType
from Plots import customPlot
from trainValidation import train, test
import numpy as np

def computeAverageDiscountReward(rewards):
    totalSum = 0
    for rewards1 in rewards:
        totalSum += computeAverageDiscountReward1(rewards1)
    return totalSum/len(rewards)

def computeAverageDiscountReward1(rewards1):
    totalSum = 0
    for rewardInEpisode in rewards1:
        totalSum += rewardInEpisode.discountedReward()
    return totalSum/len(rewards1)

def computeErrorDiscountReward(rewards):
    arr = []
    for rewards1 in rewards:
        arr.append(computeAverageDiscountReward1(rewards1))
    return np.std(arr)

num_tests = 10

epsilons = [0.01, 0.1, 0.4]
# epsilons = [0.01, 0.1]

Neps = [10, 100, 1000, 10000, 50000, 100000]
# Neps = [10]

senderRewards = None
receiverRewards = None
receiverResultsAggreagators = {}


senderResultsAggreagators = {}

for epsilon in epsilons:
    for Nep in Neps:
        allSenderRewards = []
        allReceiverRewards = []
        for testNum in range(num_tests):
            trainStatus = Settings()
            trainStatus.numberOfEpisodes = Nep
            trainStatus.senderInputSize = 4
            trainStatus.wallProbability = -10
            trainStatus.terminationProbability = 1 - 0.95
            trainStatus.wallType = WallType.fourRoom
            trainStatus.epsilon = epsilon

            sender, receiver = train(trainStatus, testNum)

            testStatus = Settings()
            testStatus.senderInputSize = 4
            testStatus.numberOfEpisodes = 1000
            testStatus.wallProbability = -10
            testStatus.terminationProbability = 1 - 0.95
            testStatus.wallType = WallType.fourRoom
            testStatus.epsilon = 0

            senderRewards, receiverRewards = test(testStatus, sender, receiver, testNum)

            allReceiverRewards.append(receiverRewards)
            allSenderRewards.append(senderRewards)
        
        receiverResultsAggreagators[(epsilon, Nep, 'mean')] = computeAverageDiscountReward(allReceiverRewards)
        senderResultsAggreagators[(epsilon, Nep, 'mean')] = computeAverageDiscountReward(allSenderRewards)

        receiverResultsAggreagators[(epsilon, Nep, 'error')] = computeErrorDiscountReward(allReceiverRewards)
        senderResultsAggreagators[(epsilon, Nep, 'error')] = computeErrorDiscountReward(allSenderRewards)

customPlot(Neps, epsilons, receiverResultsAggreagators, "receiver")
customPlot(Neps, epsilons, senderResultsAggreagators, "sender")