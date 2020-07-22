# -*- coding: utf-8 -*-
"""
    ! Informal Token Reader (Analizador Lexico Informal Demostrativo)

    *   Permite el reconocimiento de distintos tokens usando expresiones regulares para un lenguaje de 
    *   multiple instruccciones por linea de codigo. Este programa no posee lexemas de palabras especiales,
    *   en su lugar, reconocera identificadores de usuario, valores numericos, cadenas, fin de instruccion y 
    *   saltos de linea.

    *   Esta implementacion no aplica el use de"automatas finitos", lo que hacer que la implementacion 
    *   sea completamente demostrativa.

    *   Es por ello que esta demostraciOn representa un ejemplo informal para realizar el proceso de 
    *   deteccion de tokens, sobre el cual se hacen menciOn de aspectos especificos de la teoria pero no se 
    *   aplican en completitud las practicas obligatorias de la literatura, para encajar en una demostracion 
    *   dentro de la hora de clase.

    ? Comprende la logica general de la demostracion.
    ? Comprende identificadores de usuario.
    ? Comprende operador de asignaciOn.
    ? Comprende valores numericos entero y flotante.
    ? Requiere fin de instruccion.
    ? No comprende sintaxis, ni precedencia, ni comentarios, ni operadores, ni cadenas, etc.
    ? El resultado de un programa real debera ser el pipeline que alimenta al analisis sintactico
    
    @author Gabriel
    @date 2020/07/07 @version 0.1
"""
import sys,re, tabulate 
 
class InformalTokenParser:

    def __init__(self): pass

    def help(self):
        print ("")
        print ("*"*80)
        print ("*"*80)
        print ("\tInformal Token Reader (Analizador Lexico Informal Demostrativo) ")
        print ("""
        \tPermite el reconocimiento de distintos tokens usando expresiones 
        \tregulares para un lenguaje de una instrucccion por Linea de codigo. 
        \tEste programa no posee lexemas de palabras especiales, en su lugar, 
        \treconocera identificadores de usuario, valores numericos, cadenas, 
        \tfin de instruction y saltos de Linea.

        \t@author seed
        \t@date 2020/07/05 t@version 0.1""")
        print ("*"*80)
        print ("*"*80)
        print ("")

    def read(self):
        params = sys.argv[1:]
        if(len(params) != 1): quit("Error: No se ha definido el programa a ejecutar")  
        
        self.filename = params[0]
        f = open(self.filename,"r")
        self.text = f.read()
        f.close()

        return self

    def preprocess(self):
        text = self.text
        text = re.sub(r"=", " = ", text)
        text = re.sub(r";", " ; ", text)
        text = re.sub(r"\s+", " ", text)

        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text

        tokens = re.split(r'\s', text)

        for token in tokens:
            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                #Operador de asignación
                if re.match(r'^=$', token):
                    result += [["Se reconoce el operador de asignación %s" % token]]

                #Número fLotante
                elif re.match(r'^\d+\.\d+$', token):
                    result += [["Se reconoce el Número flotante %s" % token]]

                #Número entero
                elif re.match(r'^\d+$', token):
                    result += [["Se reconoce el Número Entero %s" % token]]

                #Fin de instrucción
                elif re.match(r'^;$', token):
                    result += [["Se reconoce Fin de instrucción %s" % token]]

                #Identificador de Usuario
                elif re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', token):
                    result += [["Se reconoce el identificador de usuario %s" % token]]

                #token Desconocido
                else:
                    quit("ERROR: se ha encontrado un token desconocido en la linea %d: %s" % (
                            self.searchTokenLine(token),
                            token)
                    )

        return result

        

    def searchTokenLine(self, token):
        errorLine = 0
        print("*"*80)
        print("Buscando Token: %s\n" % token)
        f = open(self.filename, "r")
        for line in f:
            errorLine += 1
            print("Debug: \tlinea %d \t%s" % (errorLine, line))
            if re.match(r"^.*%s.*$" % re.escape(token) , line):
            #if re.match(r"^.*%s.*$" % self.prevent(token) , line):
                break
        print("*"*80)
        f.close()
        return errorLine


    def prevent(self, token):
        if re.match(r"^[\+\*\.\(\)\{\}\[\]]$", token):
          return "\\%s" % token
        return token





parser = (InformalTokenParser()).read().preprocess()

parser.help()
print("\nPrograma encontrado:\n\n\t%s" % parser.filename)
print("\nPrograma preprocesado:\n\n\t%s\n" % parser.text)
lexical = parser.lexicalAnalysis()
print("El análisis lexico del Programa es: %s" % tabulate.tabulate(lexical))



#python lexicalAnalysis.py .\factorial\factorialPython.py | test.py