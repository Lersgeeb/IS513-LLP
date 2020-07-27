# -*- coding: utf-8 -*-

grammar = """
    ?start: expr+

    ?expr: "(" operation ")" 
          
    ?operation: expr 
        | "write-line" atom -> print
        | "defvar" variable -> declarevar
        | setvariable
        | arithmeticop  

    ?setvariable: "setq" variable operation -> assignvar
        | "setq" variable atom -> assignvar

    ?list: list atom
        | atom

    ?arithmeticop: "+" list -> sum
        | "*" list -> mul

    ?atom: variable -> getvar
        | string
        | number

    ?number: /\d+(.\d+)?/

    ?string: /"[^"]*"/
        | /'[^']*'/

    ?variable: /[^\(\)'",:|\s\d][^\(\)'",:|\s]+/

                
    %ignore /\s+/

"""