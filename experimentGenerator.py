from components import Question, WallType
from experiment import experiment

Neps = [10, 100, 1000, 10000, 50000, 100000]
# Neps = [10, 100]
num_tests = 10

question = Question.c

if question == Question.c:
    epsilons = [0.01, 0.1, 0.4]
    # epsilons = [0.1, 0.4]

    senderInputSizes = [4]
    wallType = WallType.fourRoom
    secondVariableName = 'epsilon'

    experiment(
        Neps=Neps,
        epsilons=epsilons,
        senderInputSizes=senderInputSizes,
        wallType=wallType,
        num_tests=num_tests,
        secondVariableName=secondVariableName
    )


elif question == Question.d:
    epsilons = [0.1]
    senderInputSizes = [2, 4, 10]
    secondVariableName = 'senderInputSize'
    wallType = WallType.fourRoom

    experiment(
        Neps=Neps,
        epsilons=epsilons,
        senderInputSizes=senderInputSizes,
        wallType=wallType,
        num_tests=num_tests,
        secondVariableName=secondVariableName
    )

elif question == Question.e:
    epsilons = [0.1]
    senderInputSizes = [2, 3, 5]
    secondVariableName = 'senderInputSize'
    wallType = WallType.maze

    experiment(
        Neps=Neps,
        epsilons=epsilons,
        senderInputSizes=senderInputSizes,
        wallType=wallType,
        num_tests=num_tests,
        secondVariableName=secondVariableName
    )

elif question == Question.f:
    epsilons = [0.1]
    senderInputSizes = [1]
    secondVariableName = 'senderInputSize'
    wallType = WallType.empty

    experiment(
        Neps=Neps,
        epsilons=epsilons,
        senderInputSizes=senderInputSizes,
        wallType=wallType,
        num_tests=num_tests,
        secondVariableName=secondVariableName
    )