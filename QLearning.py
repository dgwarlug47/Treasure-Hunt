import math


class QTable():
    def __init__(self, states, actions, numberOfEpisodes) -> None:
        self.table = {}
        self.states = states
        self.actions = actions
        self.discountFactor = 0.95
        self.startAlpha = 0.9
        self.endAlpha = 0.01
        self.numberEpisodes = numberOfEpisodes
        self.setInitialTable()

    def key(self, state, action):
        return "state:" + state.id + ", action:" + action.id

    def get(self, state, action):
        return self.table[self.key(state, action)]

    def setInitialTable(self):
        for state in self.states:
            for action in self.actions:
                self.table[self.key(state, action)] = 0

    def add(self, state, action, value):
        self.table[self.key(state, action)] = self.table[self.key(state, action)] + value

    def maxQvalue(self, state):
        maxQvalue = - math.inf
        for action in self.actions:
            maxQvalue = max(maxQvalue, self.get(state, action))
        return maxQvalue
            

    def updateTable(self, state, action, newState, reward, currentEpisode):
        currentAlpha = self.startAlpha - ((self.startAlpha) - (self.endAlpha))*(currentEpisode/self.numberEpisodes)
        value = currentAlpha * (reward + self.discountFactor*self.maxQvalue(newState) - self.get(state, action))
        self.add(state, action, value)
        

