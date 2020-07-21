# -*- coding: utf-8 -*-

from plex import *
from tabulate import tabulate
import sys

class LexicalAnalysis:

    #Str, Red, AnyBut, Any
    def __init__(self):

        #Cadena de texto /"[^"]*"/
        stringDouble = Str("\"") + Rep(AnyBut("\"")) + Str("\"")
        stringSimple= Str("'") + Rep(AnyBut("'")) + Str("'")
        
        #Espacios en blanco y comentarios
        space = Any(" \t\n")
        comment = Str("{") + Rep(AnyBut("}")) + Str("}")

        #Operadores
        assing = Str("=")
        sumOp = Str("+")

        ifKeyword = Str("if")

        self.lexicon =  Lexicon(
            [
                (stringDouble, "string"),
                (stringSimple, "string"),
                (sumOp, "sum/concat operator"),
                (assing, "assign operator"),
                (space | comment, IGNORE),
            ]
        )

        def parse(self):
            lexicon = self.lexicon
            lexicalTable = []

            filename = sys.argv[1:][0]  #[1]
            f = open(filename, "r")
            scanner = Scanner(lexicon, f, filename)

            while True:
                try:
                    token = scanner.read()

                    if not token[0]: break
                    
                    desc, val = token
                    lexicalTable += [[val, desc]]

                except Exception as e:
                    print("Lexical Error: %s" % (e) )
                    f.close()
                    return False

            f.close()
            self.lexicalTable = lexicalTable
            return self


parser = (LexicalAnalysis())

if parser.parse():
    print "Análisis Léxico: "
    print tabulate(parser.lexicalTable)    

