# -*- coding: utf-8 -*-

grammar = """
    //El axioma inicial
    ?start: exp+
    
    // Definición de una expresión
    ?exp: var "=" string ";" -> assignvar
        | var "=" arithmeticoperation ";" -> assignvar
        | "print" "("? strcat ")"? ";" -> print
        | "print" "("? var ")"? ";" -> printvar

    // Definición de operación de concatenado
    ?strcat: string
        | string "+" strcat 

    // Definición de operación aritmética
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperationatom "+" arithmeticoperationatom -> sum
        | arithmeticoperationatom "-" arithmeticoperationatom -> sub

    // Definición de un átomo de operación aritmética
    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperationatom
        | "+" arithmeticoperationatom
        | "(" arithmeticoperation ")"

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