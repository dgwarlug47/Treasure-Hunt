from operator import le
import re
from shutil import move
from numpy import rec
from scipy.stats import bernoulli
import random
import math

from Components import LearningStage, Movement, ReceiverAction

class StandardActionManagement():
    def __init__(self, qtable, actions) -> None:
        self.qtable = qtable
        self.actions = actions
        self.epsilon = 0.2

    def choose(self, state, learningStage):
        coinFlip = bernoulli(self.epsilon).rvs(1)[0]

        if (coinFlip == 0 and learningStage == LearningStage.train):
            return random.choice(self.actions)
        else:
            return self._bestAction(state)
    
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