# -*- coding: utf-8 -*-
"""
    ! Analizador Léxico

    * Programa principal cuya funcionalidad se basa en ejecutar el análisis léxico de un código escrito en c++  
    
    ? Imprimirá una lista de todos los token encontrados junto con la descripción detallada respectiva
    ? Al encontrar un error imprime el número de línea donde ha sido encontrado el error junto al carácter que lo ha provocado

    @author Gabriel
    @date 2020/07/19 
    @version 0.1
"""

from Core.LexicalAnalyzer import LexicalAnalyzer

lexical = LexicalAnalyzer()

lexical.run()
lexical.printLexemDesc()