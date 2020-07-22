# -*- coding: utf-8 -*-
from DFA import DFA
from Reader import Reader


"""
    !String Finder Automata
    * Clase que extiende a la clase abstracta de DFA añadiendo funcionalidades que permiten 
    * la identificacion de cadenas dentro de un archivo de texto

    ? Para una mayor comprension mirar el diagrama de estado dentro de los archivos
    
    ? EXPLICACION DE CADA ESTADO
    ? q0: Estado donde se espera el caracter (') o (") para entrar en la fase de comentario 
    ? q1: Estado donde se guardan todos los caracteres exceptuando (")
    ? q2: Estado donde se guardan todos los caracteres exceptuando (')
    ? q3: Estado que escapa de la fase de comentario y guarda la cadena de todos los caracteres almacenados

    @author Gabriel
    @date 2020/07/15 @version 0.1
"""

class StringFinderAutomata(DFA):  
    
    #crea un automata en especifico cuya tarea sera encontrar strings 
    def __init__(self):
        states = ['q0','q1','q2','q3']
        transitions = {
            'q0':{'"':'q1',"'":'q2',super().ASCII:'q0'},
            'q1':{'"':'q3',super().ASCII:'q1'},
            'q2':{"'":'q3',super().ASCII:'q2'},            
            'q3':{'"':'q1',"'":'q2',super().ASCII:'q0'},
        }
        finalstate = {'q3':'COMMENT'}

        super().__init__(states, transitions, 'q0',finalstate)
        self.reader = ( Reader() ).read()
        
    #Lee caracter por caracter y determina el estado del automata.
    #Cuando el programa entra en el estado q1 o q2 se guardan los caracteres en una memoria temporal.
    #Cuando el programa entra en el estado q3 guarda todos los caracteres almacenados como cadena en una lista.
    def stringAutomata(self):
        self.stringsList = []
        stringTemp = []
        char = self.reader.nextChar()
        while char:
            print("Cambiar estado %s con el caracter: %s" % (self.getStateName() ,char))
            if(char):
                self.changeState(char)
            
            if self.getStateName() == 'q1':
                # Entrar en comentario
                if not char == '"':
                    stringTemp += char

            if self.getStateName() == 'q2':
                # Entrar en comentario
                if not char == "'":
                    stringTemp += char

            if self.getStateName() == 'q3':
                # Entrar de comentario y guardar string
                self.stringsList += ["".join(stringTemp)]
                stringTemp = []

            char = self.reader.nextChar()

        return self.stringsList

