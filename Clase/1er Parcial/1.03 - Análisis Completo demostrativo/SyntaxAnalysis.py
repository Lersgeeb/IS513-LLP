"""
    ! Syntax Analysis (Analizador Sintáctico Demostrativo)
    ! Non-CFG

    * Permite el reconocimiento de distintos tokens en el orden
    * correcto de instrucciones.

    ? Comprende Identificadores de usuario
    ? Comprende operador de asignación
    ? Comprende valores numéricos y flotantes
    ? Requiere fin de instrucción
    ? Se comunica mediante pipeline
"""

# *-* coding: utf-8 *-*
import re

class SyntaxAnalysis:
    def __init__(self): pass

    def read(self):
        self.text = input()
        return self

    def parse(self):
        text = self.text
        lines = re.split(r";", text)

        for i in range( len(lines) ):
            
            line = ("%s".strip() % lines[i]).strip()
            
            if len(line) > 0:
                if(
                    re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s=\s*\d+(\.\d+)?$", line) or
                    re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s=\s*[a-zA-Z][a-zA-Z\d_]*$", line)
                ):
                    pass
                else:
                    quit("Error sintáctico: se ha encontrado un error en la línea %d" % i)
        
        return True


parser = (SyntaxAnalysis()).read()

if parser.parse():
    print( "%s" % parser.text)

