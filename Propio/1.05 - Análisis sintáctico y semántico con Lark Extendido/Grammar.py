# -*- coding: utf-8 -*-

grammar = """
    //El axioma inicial
    ?start: exp+
    
    // Definición de una expresión
    ?exp: var "=" string ";" -> assignvar
        | var "=" expr ";" -> assignvar
        | "print" "(" stringoperation ")" ";" -> print
        | "print" stringoperation ";" -> print

    // Definición de operación de concatenado
    ?stringoperation: string
        | var -> getvar
        | var "+" stringoperation -> catstringvar
        | string "+" stringoperation -> catstrings

    // Definición de operación aritmética
    ?expr: term "+" expr -> sum
        | expr "-" term -> sub
        | term

    ?term: term "*" factor -> mul
        | factor "/" expr -> div
        | factor

    ?factor: "(" expr ")"
        | number
        | var -> getvar

    // Definición de una cadena
    ?string: /"[^"]*"/
        | /'[^']*'/

    // Definición de una variable
    ?var: /[a-zA-Z]\w*/

    // Definición de un nómero
    ?number: /\d+(\.\d+)?/

    //Ignorar espacios, saltos de línea y tabulados
    %ignore /\s+/


"""