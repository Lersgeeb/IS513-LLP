# -*- coding: utf-8 -*-

from plex import *
from tabulate import tabulate
import sys

class LexicalAnalysis:

    def __init__(self):

        letter = Range("AZaz")
        digit = Range("09")

        #Declarar la forma de un identificador
        ident = letter + Rep(letter|digit)

        #Declarar una Asignación 
        assign = Str("=")

        #Declarar operaciones         
        operation = Any("+-*/%")

        #Declarar Cadenas
        singleQuoteString = Str("'") + Rep(AnyBut("'")) + Str("'")
        doubleQuoteString = Str("\"") + Rep(AnyBut("\"")) + Str("\"")

        #Declarar Palabras reservadas 
        keywords = Str("print","if", "else")

        #declarar operaciones condicionales
        conditionalOperation = Str(">", "<", "==", "!=", "<=", ">=" )
        
        #Declarar Parentesis y llaves
        paranthesis = Any("()")
        brackets = Any("}{")

        #Declarar mas simbolos
        endOfIns = Any(";")
        separateArgs = Any(",")

        #spaces
        space = Any(" \n\t")

        #comment
        commentByLine = Str("#") + Rep(AnyBut("\n")) 

        self.lexicon = Lexicon(
            [
                (digit, "LIT_INTEGER"),
                (assign, "ASSIGN_OP"),
                (operation, "ARITHMETIC_OP"),
                (singleQuoteString | doubleQuoteString, "STRING"),
                (keywords, "KEYWORD_IDENT"),
                (conditionalOperation, "CONDITIONAL_OP"),
                (paranthesis| brackets | endOfIns | separateArgs,  "STMT_SYMBL"),
                (ident, "IDENTIFIER"),
                (space| commentByLine, IGNORE)
            ]
        )

    def parse(self):
        lexicon = self.lexicon
        lexicalTable = []

        filename = sys.argv[1:][0]

        f = open(filename, "r")

        scanner = Scanner(lexicon, f, filename)

        while(True):

            try:
                token = scanner.read()

                if(not token[0]): break

                desc, val = token
                lexicalTable += [[val, desc]]

            except Exception as e:
                f.close()
                print("LEXICAL ERROR: %s" % e)
                return False

        f.close()
        self.lexicalTable = lexicalTable
        return self


parser = (LexicalAnalysis())
if parser.parse():
    print("Analisis Lexico")
    print(tabulate(parser.lexicalTable))
