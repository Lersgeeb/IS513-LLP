class State:

    DIGIT = '0123456789'
    ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\\]^_`abcdefghijklmnñopqrstuvwxyz{|}~'
    
    def __init__(self, name, finalState = None):
        self.name = name
        self.finalState = finalState
        self.transitions = {}
        
    #Dado un caracter se estblecera  un movimiento de
    def setTransition(self, char, state):
        self.transitions[char] = state

    #Dependiendo del character dado retornara un estado especifico 
    def StateTransition(self, char):
        if char in self.transitions.keys():
            return  self.transitions[char]

        elif( (char in State.ALPHA) and (State.ALPHA in self.transitions.keys()) ):
            return self.transitions[State.ALPHA]
        
        elif( (char in State.DIGIT) and (State.DIGIT in self.transitions.keys()) ):
            return self.transitions[State.DIGIT]
            
        else:
            return self.transitions[State.ASCII]


