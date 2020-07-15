# -*- coding: utf-8 -*-
"""
    ! Token Reader (Analizador Lexico)

    * Reconocimiento de token basado en los conceptos planteados por el libro de lenguajes de programación 
    * El presente analizador lexico solo reconocera elementos de asignacion, identificadores , numeros literales y enteros 

    ? Pasos  
    ? Crear las diferentes clases/estados en el que el caracter puede estar


    @author Gabriel
    @date 2020/07/17 @version 0.1
"""

import sys,re

class TokenParser:
    #Clases
    LETTER = "letter"
    DIGIT = 'digit'
    UNKNOWN = 'unknown'


    #Token
    '''
    INT_LIT = 10
    IDENT = 11
    ASSIGN_OP = 20
    ADD_OP = 21
    SUB_OP = 22
    MULT_OP = 23
    DIV_OP = 24
    '''
    OPERATION = 'opert_Token'
    LEFT_PAREN = 'left_Paren'
    RIGHT_PAREN = 'rigth_Paren'

    def __init__(self): pass


    def setup(self):
        self.lexem = []
        self.lexemes = {}
        
        params = sys.argv[1:]
        if(len(params) != 1): 
            quit("Error: No se ha definido el programa a ejecutar")  

        self.filename = params[-1]

        f = open(self.filename, 'r')
        self.text = f.read()
        f.close

        return self

    def preprocess(self):
            text = re.sub(r"\s+", " ", self.text)
            self.text = ("%s".strip() % text).strip()
            self.textList = list(self.text)

            return self

    #Function to determine character class
    def getClassChar(self, char):
        if re.match(r"[A-Za-z]", char):
            return TokenParser.LETTER
        
        elif re.match(r"[\d]", char):
            return TokenParser.DIGIT

        else:
            return TokenParser.UNKNOWN

    #Function to get the next character of input 
    def getNextChar(self):
        return self.textList.pop(0)

    #Function to skip blank space
    def getNonBlankChar(self):
        char = self.textList.pop(0)
        while re.match(r"\s", char):
            char = self.textList.pop(0)
        return char

    #lookup - a function to lookup operators and parentheses and return the token
    def lookup(self, char):
        if re.match(r'^[\+\-\*\/]\*?$', char):
            self.lexem = [char]
            self.token = TokenParser.OPERATION

    def lexicAnalysis(self):
        pass


parser = (TokenParser()).setup().preprocess()
print(parser.getClassChar('<'))

parser.lookup('+')
print(parser.lexem)
print(parser.token)

    