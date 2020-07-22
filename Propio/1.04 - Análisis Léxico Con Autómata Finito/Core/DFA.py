# -*- coding: utf-8 -*-
from Core.State import State

"""
    ! Clase Abstracta de un Automata Finito Determinista

    ? Cuenta con las funcionalidades basicos para manipular el automata
    ? Brinda la posibilidad de crear cualquier autómata dado un conjunto de estados con sus transiciones respectivas

    @author Gabriel
    @date 2020/07/19 @version 0.1
"""

class DFA:

    DIGIT = '0123456789'
    ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\\]^_`abcdefghijklmnñopqrstuvwxyz{|}~'

    #Inicializa el DFA creando los estados y estableciendo todas las transiciones 
    def __init__(self, states, transitions, initialState, finalState = {}):  
        self.states = {}
        for state in states:
            if state in finalState.keys():
                self.states[state] = State(state, finalState[state])
            else:
                self.states[state] = State(state)

        
        for state,transition in transitions.items():
            for char,stateAim in transition.items():
                self.states[state].setTransition(char, self.states[stateAim])

        self.currentState = self.states[initialState]

    #Cambia el estado dependiendo del caracter leido
    def changeState(self,char):
        self.currentState = self.currentState.StateTransition(char)

    #Verifica si el estado actual es un estado final
    def isFinalState(self):
        if(self.currentState.finalState):
            return True
        else: return False
            
    #Obtener el valor de estadoFinal
    def getFinalState(self):
        return self.currentState.finalState
    
    #Obtener el nombre de estado
    def getStateName(self):
        return self.currentState.name
    

    


