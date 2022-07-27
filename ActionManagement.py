from scipy.stats import bernoulli
import random
import math

from components import LearningStage, Movement, ReceiverAction
from qLearning import QTable

class StandardActionManagement():
    def __init__(self, states, actions, numberOfEpisodes, epsilon) -> None:
        self.qtable = QTable(states, actions, numberOfEpisodes)
        self.actions = actions
        self.epsilon = epsilon

    def choose(self, state, learningStage):
        coinFlip = bernoulli(self.epsilon).rvs(1)[0]

        if (coinFlip == 1 and learningStage == LearningStage.train):
            return random.choice(self.actions)
        else:
            return self.bestAction(state)
    
    def updateQtable(self, state, action, newState, reward, currentEpisode):
        self.qtable.updateTable(state, action, newState, reward, currentEpisode)

    def bestAction(self, state):
        bestAction = None
        bestQValue = - math.inf
        for action in self.actions:
            if (bestQValue < self.qtable.get(state, action)):
                bestAction = action
                bestQValue = self.qtable.get(state, action)

        if (bestAction == None):
            print("what is going on?")
            assert(False)
        return bestAction

class CheatReceiverActionManagement():
    def choose(self, receiverState, senderState):
        if (receiverState.currentX < senderState.xprize):
            return ReceiverAction(Movement.right)
        elif (receiverState.currentX > senderState.xprize):
            return ReceiverAction(Movement.left)
        elif (receiverState.currentY < senderState.yprize):
            return ReceiverAction(Movement.down)
        elif (receiverState.currentY > senderState.yprize):
            return ReceiverAction(Movement.up)
        else:
            assert(False)