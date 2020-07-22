# -*- coding: utf-8 -*-
from StringFinderAutomata import StringFinderAutomata

"""
    !String Automata
    * El siguiente Programa crea un Automata Finito Determinista que identifica
    * Cadenas encerradas entre comillas tales como (') o (").

    * Dado un parametro desde la ejecucion de consola el programa lee un archivo y retorna una 
    * lista todas las cadenas encontradadas

    ? Probar codigo con los comandos: 
    ?   <python main.py sample.lng> 
    ?   <python main.py sample2.lng>

    ? Expresion regular del automata
    ?  r"(\"[^"]*\")|('[^']*')"


    @author Gabriel
    @date 2020/07/15 @version 0.1
"""

SFA = StringFinderAutomata()
stringsList = SFA.stringAutomata()

print("las strings encontradas son: \n", stringsList)



