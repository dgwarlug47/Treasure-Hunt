from operator import le
import re
from shutil import move
from numpy import rec
from scipy.stats import bernoulli
import random
import math

from Components import LearningStage, Movement, ReceiverAction
from QLearning import QTable

class StandardActionManagement():
    def __init__(self, states, actions, numberOfEpisodes, epsilon) -> None:
        self.qtable = QTable(states, actions, numberOfEpisodes)
        self.actions = actions
        self.epsilon = epsilon

    def choose(self, state, learningStage):
        coinFlip = bernoulli(self.epsilon).rvs(1)[0]

        if (coinFlip == 0 and learningStage == LearningStage.train):
            return random.choice(self.actions)
        else:
            return self._bestAction(state)
    
    def updateQtable(self, state, action, newState, reward, currentEpisode):
        self.qtable.updateTable(state, action, newState, reward, currentEpisode)

    def _bestAction(self, state):
        bestAction = None
        bestQValue = - math.inf
        for action in self.actions:
            if (bestQValue > self.qtable.get(state, action)):
                bestAction = action
                bestQValue = self.qtable.get(state, action)
        return bestAction

class CheatReceiverActionManagement():
    def choose(self, receiverState, senderState):
        if (receiverState.currentX < senderState.xprize):
            return ReceiverAction(Movement.right)
        if (receiverState.currentX > senderState.xprize):
            return ReceiverAction(Movement.left)
        if (receiverState.currentY < senderState.yprize):
            return ReceiverAction(Movement.down)
        if (receiverState.currentY > senderState.yprize):
            return ReceiverAction(Movement.up)