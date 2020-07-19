# -*- coding: utf-8 -*-
"""
    ! Analizador Lexico

    * Reconocimiento de token

    ? Pasos  
    ? 


    @author Gabriel
    @date 2020/07/19 @version 0.1
"""

from DFA import DFA
from Reader import Reader
from DesignedLexicalAutomata import DesignedLexicalAutomata
from LexemeDesc import LexemeDesc
import tabulate

class LexicalAutomata(DFA):  
    
    #crea un automata en especifico cuya tarea sera encontrar strings 
    def __init__(self):

        super().__init__(DesignedLexicalAutomata.STATES, DesignedLexicalAutomata.TRANSITIONS, 'start')
        self.reader = ( Reader() ).read()
        self.lexDesc = LexemeDesc()
        self.lineCount = 1
        self.error = False


    def run(self, debug = False):
            self.tokenDesc = []
            stringTemp = []
            char = self.reader.nextChar()
            prevState = 'start'
            
            while char:
                
                if(debug):
                    print("Cambiar estado %s con el caracter: %s" % (self.getStateName() ,char))

                if(char):
                    prevState = self.getStateName()
                    self.changeState(char)
                    actualState = self.getStateName()

                    if(char == '\n'):
                        self.lineCount += 1


                if(actualState=='error'):
                    self.error = "ERROR: se ha encontrado un token desconocido en la linea %s: %s" % (self.lineCount, char)
                    quit(self.error)

                elif(actualState=='waitFloat'):
                    stringTemp += char
                
                elif(prevState=='waitFloat' and actualState=='float'):
                    stringTemp += char
                
                elif(actualState=='waitString1' or actualState=='waitString2'):
                    if(len(stringTemp) < 20):
                        stringTemp += char
                
                elif(actualState=='string'):
                    if(len(stringTemp) == 20):
                        stringTemp += ['.','.','.']

                    stringTemp += char
                    if(len(stringTemp) > 0):
                        self.tokenDesc += [self.getDescription(actualState,"".join(stringTemp))]
                    stringTemp = []


                elif(prevState != actualState and actualState=='lookup'):
                    if(len(stringTemp) > 0):
                        self.tokenDesc += [self.getDescription(prevState,"".join(stringTemp))]
                    self.tokenDesc += [self.getDescription(actualState, char)]
                    stringTemp = []
                
                elif( prevState != actualState):
                    if(len(stringTemp) > 0):

                        self.tokenDesc += [self.getDescription(prevState,"".join(stringTemp))]
                    stringTemp = []
                    if(char != ' '):
                        stringTemp += char               
                
                elif(actualState=='lookup'):
                     self.tokenDesc += [self.getDescription(actualState, char)]
                     stringTemp = []

                else:
                   if(char != ' ' or char != ''):
                        stringTemp += char

                char = self.reader.nextChar()

            


    def getDescription(self, state, lexem):
        
        if(state=='ident'):
            return self.lexDesc.isKeyword(lexem)

        elif(state=='operator'):
            return self.lexDesc.operator(lexem)

        elif(state=='conditionAssign'):
            return self.lexDesc.conditionAssign(lexem)

        elif(state=='classToken'):
            return self.lexDesc.classToken(lexem)

        elif(state=='lookup'):
            return self.lexDesc.lookup(lexem)
        
        elif(state=='string'):
            return self.lexDesc.stringDesc(lexem)
        
        elif(state=='float'):
            return self.lexDesc.floatDesc(lexem)
        
        elif(state=='int'):
            return self.lexDesc.intDesc(lexem)

                
    def printLexemDesc(self):
        if(not self.error):
            tokenDescClean = [
                ['#','Token', 'Descripción', 'Lexema'],
                ['--', '---------', '--------------------------------------', '------------------------']
            ]
            for desc in self.tokenDesc:
                if(desc):
                    tokenDescClean.append(desc)

            print(tabulate.tabulate(tokenDescClean))
    
        else:
            print(self.error)


lexical = LexicalAutomata()

lexical.run()
lexical.printLexemDesc()