from Components import Settings, WallType
from trainValidation import train, test
def computeDiscountReward (rewards):
    return sum(rewards) / len(rewards)

num_tests = 10

espsilons = [0.01, 0.1, 0.4]

#Neps = [10, 100, 1000, 10000, 50000, 100000]
Neps = [100]

senderRewards = None
receiverRewards = None

for epsilon in espsilons:
    for Nep in Neps:
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