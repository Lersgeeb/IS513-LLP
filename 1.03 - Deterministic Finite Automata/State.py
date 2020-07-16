class State:

    def __init__(self, name, finalState = None):
        self.name = name
        self.finalState = finalState
        self.transitions = {}
        
    def setTransition(self, char, state):
        self.transitions[char] = state

    def shift(self, char):
        return  self.transitions[char]

