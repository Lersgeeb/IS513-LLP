# -*- coding: utf-8 -*-

from Reader import Reader
from Automata import Automata
import tabulate

reader = (Reader()).read()
automata = (Automata(reader)).run()

tokensInfo = []
print("\n\nresultado: \n")
for token in automata.tokens:
    
    value, valueType = token.info()
    tokensInfo += [[value, valueType]]

print(tabulate.tabulate(tokensInfo))

