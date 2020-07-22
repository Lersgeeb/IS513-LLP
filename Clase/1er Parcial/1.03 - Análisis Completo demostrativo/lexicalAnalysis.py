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
        text = re.sub(r"=", " = ", self.text)
        text = re.sub(r";", " ; ", text)
        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"#(\s?\w*\s?)*", " #comment ", text)
        text = re.sub(r"(((\'\'\')|(\"\"\"))(\s?\w*\s?)*)((\'\'\')|(\"\"\"))", "\'\'\'comment\'\'\'", text)
        text = re.sub(r":", " : ", text)
        text = re.sub(r"\s[\'\"]{1,1}[\w\%\!\@\#\$\^\&\*\(\)0-9\s]*[\'\"]\s", " \'string\' ", text)

        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text
        tokens = re.split(r'\s', text)
        for token in tokens:
            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                #Palabra reservada
                if re.match(r'^def$', token):
                    result += [["Se reconoce plabra reservada %s" % token]]

                #Operador de asignación
                elif re.match(r'^=$', token):
                    result += [["Se reconoce el operador de asignación %s" % token]]

                #Número fLotante
                elif re.match(r'^\d+\.\d+$', token):
                    result += [["Se reconoce el Número flotante %s" % token]]

                #Número Entero
                elif re.match(r'^\d+$', token):
                    result += [["Se reconoce el Número Entero %s" % token]]

                #Fin de instrucción
                elif re.match(r'^;$', token):
                    result += [["Se reconoce Fin de instrucción %s" % token]]

                #Comentario
                elif re.match(r'^(#comment)|(\'\'\'comment\'\'\')$', token):
                    result += [["Se reconoce Comentario %s" % token]]

                #colon 
                elif re.match(r'^:$', token):
                    result += [["Se reconoce Colon  %s" % token]]
                    
                #if
                elif re.match(r'^if$', token):
                    result += [["Se reconoce palabra reservada  %s" % token]]

                #return 
                elif re.match(r'^return$', token):
                    result += [["Se reconoce palabra reservada %s" % token]]

                #modulo
                elif re.match(r'^%$', token):
                    result += [["Se reconoce modulo  %s" % token]]

                #modulo
                elif re.match(r'^,$', token):
                    result += [["Se reconoce coma  %s" % token]]

                #operación parentesis
                elif re.match(r'^\)$', token):
                    result += [["Se reconoce parentesis derecho  %s" % token]]

                elif re.match(r'^\($', token):
                    result += [["Se reconoce parentesis izquierdo  %s" % token]]

                #operación condicional
                elif re.match(r'^((<=?)|(>=?)|(<?)|(>?)|(==)|(!=))$', token):
                    result += [["Se reconoce operación condicional  %s" % token]]

                #operación aritmetica
                elif re.match(r'^[\+\-\*\/]\*?$', token):
                    result += [["Se reconoce operación aritmetica  %s" % token]]

                #string
                elif re.match(r'^\'string\'$', token):
                    result += [["Se reconoce String  %s" % token]]

                #Identificador de Usuario
                elif re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', token):
                    result += [["Se reconoce el identificador de usuario %s" % token]]

                #token Desconocido
                else:
                    #quit()
                    return (
                        "ERROR: se ha encontrado un token desconocido en la linea %d: %s" % (
                            self.searchTokenLine(token),
                            token
                        )
                    )

        #return result
        return self.text

    def searchTokenLine(self, token):
        errorLine = 0
        #print("*"*80)
        #print("Buscando Token: %s\n" % token)
        f = open(self.filename, "r")
        for line in f:
            errorLine += 1
            #print("Debug: \tlinea %d \t%s" % (errorLine, line))
            if re.match(r"^.*%s.*$" % re.escape(token) , line):
            #if re.match(r"^.*%s.*$" % self.prevent(token) , line):
                break
        #print("*"*80)
        f.close()
        return errorLine


    def prevent(self, token):
        if re.match(r"^[\+\*\.\(\)\{\}\[\]]$", token):
          return "\\%s" % token
        return token





parser = (InformalTokenParser()).read().preprocess()

'''
parser.help()
print("\nPrograma encontrado:\n\n\t%s" % parser.filename)
print("\nPrograma preprocesado:\n\n\t%s\n" % parser.text)
lexical = parser.lexicalAnalysis()
print("El análisis lexico del Programa es: %s" % tabulate.tabulate(lexical))
'''

lexical = parser.lexicalAnalysis()
print(lexical)


#python lexicalAnalysis.py .\factorial\factorialPython.py | test.py