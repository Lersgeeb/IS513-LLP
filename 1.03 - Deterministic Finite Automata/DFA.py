# -*- coding: utf-8 -*-
from State import State

class DFA:

    DIGIT = '0123456789'
    ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, states, transitions, initialState, alphabet = True):  
        self.states = {}
        for state in states:
            self.states[state] = State(state)
        
        for state,transition in transitions.items():
            for char,stateAim in transition.items():
                self.states[state].setTransition(char, self.states[stateAim])

        self.currentState = self.states[initialState]

     
    def readChar(self,char):
        self.currentState = self.currentState.shift(char)


states = ['A','B','C','D','E']

transitions = {
    'A':{'0':'B','1':'A'},
    'B':{'0':'C','1':'A'},
    'C':{'0':'C','1':'D'},
    'D':{'0':'C','1':'E'},
    'E':{'0':'E','1':'E'},
}


DFA = DFA(states, transitions, 'A')
print(DFA.currentState.name)
DFA.readChar('0')
print(DFA.currentState.name)
