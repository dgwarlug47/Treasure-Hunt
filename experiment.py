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

def experiment(Neps, epsilons, senderInputSizes, wallType, num_tests, secondVariableName):
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
                    receiverResultsAggreagators[(Nep, epsilon, 'mean')] = computeAverageDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(Nep, epsilon, 'mean')] = computeAverageDiscountReward(sameConfigSenderRewards)

                    receiverResultsAggreagators[(Nep, epsilon, 'error')] = computeErrorDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(Nep, epsilon, 'error')] = computeErrorDiscountReward(sameConfigSenderRewards)

                elif secondVariableName == 'senderInputSize':
                    receiverResultsAggreagators[(Nep, senderInputSize, 'mean')] = computeAverageDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(Nep, senderInputSize, 'mean')] = computeAverageDiscountReward(sameConfigSenderRewards)

                    receiverResultsAggreagators[(Nep, senderInputSize, 'error')] = computeErrorDiscountReward(sameConfigReceiverRewards)
                    senderResultsAggreagators[(Nep, senderInputSize, 'error')] = computeErrorDiscountReward(sameConfigSenderRewards)
                else:
                    assert(False)

    if secondVariableName == 'epsilon':
        customPlot(Neps, epsilons, secondVariableName, receiverResultsAggreagators, "receiver")
        customPlot(Neps, epsilons, secondVariableName, senderResultsAggreagators, "sender")
    elif secondVariableName == 'senderInputSize':
        customPlot(Neps, senderInputSizes, secondVariableName, receiverResultsAggreagators, "receiver")
        customPlot(Neps, senderInputSizes, secondVariableName, senderResultsAggreagators, "sender")
    else:
        assert(False)
    
    print("receiverResultsAggregators", receiverResultsAggreagators)
    print("senderResultsAggregators", senderResultsAggreagators)