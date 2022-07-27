from components import ReceiverAction
from plots import customPlot
from experimentSetting import getTrainTestStatus
from policyUI import policyUI
from trainTest import train, test
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

def experiment(Neps, epsilons, senderInputSizes, wallType, num_tests, secondVariableName):
    testSenderRewards = None
    testReceiverRewards = None
    receiverResultsAggreagators = {}


    senderResultsAggreagators = {}

    for epsilon in epsilons:
        for Nep in Neps:
            for senderInputSize in senderInputSizes:
                sameConfigSenderRewards = []
                sameConfigReceiverRewards = []
                for testNum in range(num_tests):
                    trainStatus, testStatus = getTrainTestStatus(Nep, epsilon, senderInputSize, wallType)
                    sender, receiver = train(trainStatus, testNum)
                    policyUI(receiver, trainStatus.senderInputSize)

                    testSenderRewards, testReceiverRewards = test(testStatus, sender, receiver, testNum)
                    sameConfigReceiverRewards.append(testReceiverRewards)
                    sameConfigSenderRewards.append(testSenderRewards)
                
                if secondVariableName == 'epsilon':
                    receiverResultsAggreagators[(epsilon, Nep, 'mean')] = computeAverageDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(epsilon, Nep, 'mean')] = computeAverageDiscountReward(sameConfigSenderRewards)

                    receiverResultsAggreagators[(epsilon, Nep, 'error')] = computeErrorDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(epsilon, Nep, 'error')] = computeErrorDiscountReward(sameConfigSenderRewards)

                elif secondVariableName == 'senderInputSize':
                    receiverResultsAggreagators[(senderInputSize, Nep, 'mean')] = computeAverageDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(senderInputSize, Nep, 'mean')] = computeAverageDiscountReward(sameConfigSenderRewards)

                    receiverResultsAggreagators[(senderInputSize, Nep, 'error')] = computeErrorDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(senderInputSize, Nep, 'error')] = computeErrorDiscountReward(sameConfigSenderRewards)
                
                else:
                    assert(False)

    if secondVariableName == 'epsilon':
        customPlot(Neps, epsilons, secondVariableName, receiverResultsAggreagators, "receiver")
        customPlot(Neps, epsilons, secondVariableName, senderResultsAggreagators, "sender")
    elif secondVariableName == 'senderInputSize':
        customPlot(Neps, senderInputSizes, secondVariableName, receiverResultsAggreagators, "receiver")
        customPlot(Neps, senderInputSize, secondVariableName, senderResultsAggreagators, "sender")
    else:
        assert(False)