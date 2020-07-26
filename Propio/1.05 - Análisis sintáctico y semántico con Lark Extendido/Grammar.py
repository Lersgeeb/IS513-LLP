# -*- coding: utf-8 -*-

grammar = """
    //El axioma inicial
    ?start: exp+
    
    // Definición de una arithmeticxpr
    ?exp: var "=" arithmeticexpr ";" -> assignvar  
        | printfun ";" 

    ?printfun: "print" arithmeticexpr -> print
        | "print" "(" string "%" "(" parameters ")" ")" -> printf
        | "print" string "%" "(" parameters ")" -> printf
    
    // Definición de operación aritmética
    ?arithmeticexpr: term
        | term "+" arithmeticexpr -> plusop
        | arithmeticexpr "-" term -> sub
        
    ?term: factor
        | term "*" factor -> mul
        | term "/" factor -> div
        
    
    ?factor: atom
        | "(" arithmeticexpr ")"

    ?atom:number
        | var -> getvar
        | string  

    //Parameters
    ?parameters: 
        | var "," parameters -> arguments
        | string "," parameters -> arguments
        | number "," parameters -> arguments
        | var 
        | string 
        | number 
    
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