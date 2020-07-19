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

from DFA import DFA
from Reader import Reader

class LexicalAutomata(DFA):  
    
    #crea un automata en especifico cuya tarea sera encontrar strings 
    def __init__(self):
        states = [
            'start',
            'ident',
            'int',
            'waitFloat',
            'float',
            'operator',
            'conditionAssign',
            'classToken',
            'lookup',
            'waitString1',
            'waitString2',
            'string',
        ]

        transitions = {
            'start':{
                super().ALPHA:'ident',
                super().DIGIT:'int',
                super().ASCII:'start', 
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ':':'classToken',
                ';{(})#,.':'lookup',
                '"':'waitString1',
                "'":'waitString2',
            },
            
            'ident':{
                super().ALPHA:'ident',
                super().DIGIT:'ident',
                super().ASCII:'start',
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ':':'classToken',
                ';{(})#,.':'lookup',
            },
            
            'int':{
                super().DIGIT:'int',
                super().ASCII:'start',
                '.':'waitFloat',
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ':':'classToken',
                ';{(})#,':'lookup',
            },
            
            'waitFloat':{super().DIGIT:'float'},
            'float':{
                super().DIGIT:'float',
                super().ASCII:'start', 
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ':':'classToken',
                ';{(})#,.':'lookup',
            },
            
            'operator':{
                super().ALPHA:'ident',
                super().DIGIT:'int',
                super().ASCII:'start',
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ':':'classToken',
                ';{(})#,.':'lookup',
            },
            
            'conditionAssign':{
                super().ALPHA:'ident',
                super().DIGIT:'int',
                super().ASCII:'start',
                '=':'conditionAssign', 
                ':':'classToken',
                ';{(})#,.':'lookup',
            },

            'classToken':{
                super().ALPHA:'ident',
                super().DIGIT:'int',
                super().ASCII:'start',
                ":":"classToken",
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ';{(})#,.':'lookup',
            },

            'lookup':{
                super().ALPHA:'ident',
                super().DIGIT:'int',
                super().ASCII:'start',
                ":":"classToken",
                '/*-+^%':'operator',
                '=><!':'conditionAssign',
                ';{(})#,.':'lookup',
            },

            'waitString1':{
                '"':'string',
                super().ASCII:'waitString1'
            },
            'waitString2':{
                "'":'string',
                super().ASCII:'waitString2'
            },            
            'string':{
                '"':'waitString1',
                "'":'waitString2',
                super().ASCII:'start'
            },

        }
        #finalstate = {'q3':'COMMENT'}

        super().__init__(states, transitions, 'start')
        self.reader = ( Reader() ).read()


    def run(self, debug = False):
            self.stringsList = []
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
                    

                if( (prevState != actualState and prevState != 'start') or actualState=='lookup'):
                    self.stringsList += ["".join(stringTemp)]
                    stringTemp = []
                    stringTemp += char

                else:
                    stringTemp += char




                char = self.reader.nextChar()

            print(self.stringsList)

lexical = LexicalAutomata()

lexical.run(True)