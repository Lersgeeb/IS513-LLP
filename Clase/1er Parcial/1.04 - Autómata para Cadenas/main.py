# -*- coding: utf-8 -*-

from Reader import Reader
from Automata import Automata

reader = (Reader()).read()
automata = (Automata(reader)).run()

print ( "\n\nResultados: ")
for token in automata.tokens:

    value, valueType = token.info()
    print ("\t%s - %s" % (value, valueType))
   