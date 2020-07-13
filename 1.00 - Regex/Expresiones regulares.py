
"""

Regular Expressions
=====================
    
    Son una simbologia que permite que atraves de una nomenclatura permite el reconocimiento de patrones de texto.

    La simbologia del RegExp esta compuesta por metacaracteres los cuales tienen una funcion especifica para reconocer el patron.

    Un ejemplo baisoco es el de busqueda de archivos en la computadora, cuando el usuario usa el simbolo asterisco como un comodin.


    http://regexr.com

        En la caja de texto grande escriba:
            Hola mundo.
        
        En caja de texto pequeña:
            /ola/

    Caracteres Especiales en las RegEXp
    ------------------------------------

    Son aquellos que tienene un significado no literal dentro de la expresion regular.
        . * { } [ ] / - + ( ) ?
    
    Metacaracteres 
    --------------

    Son una combinacion de caracteres especiales que tiene un significado superrior dentro de la expresion regular.

        \w: Un caracter alfanumerico o guion baho
        \W: Un caracter que no es \w.
        \d: Un caracter numerico (i.e: un digito)
        \D: Un caracter que no es \d
        []: Significa un unico caracter que puede ser cualquier de los caracteres que se encuentran dentro de los corchetes 
        (): Agrupar.
        {}: Repeticion.
            {n}: Se repite especificamente n veces
            {n,m}: se repite al menos n veces y maximo m veces.
            {n,}: Se repite al menos n veces, maximo infinitas veces.
            {,m}: Se repite maximo m veces.
        . : Significa "Cualquier caracter".
        *: El caracter o la agrupacion anterior se repite cero o infinitas veces.
        +: El caracter o la agrupacion anterior se repite 1 o infinitas veces.
        ?: el caracter o agrupacion anterior es opcional.

    Ejemplo
    --------

    Una expresion regular para reconocer el siguient enumero de telefono:

        9213-2121
            Numero de Honduras.
            Originalmente era del operador Tigo.
            Telefonia movil.

        (\(\+504\))?\d\d\d\d-?\d\d\d\d
        (\(\+504\))?9\d{3}-?\d{4}

        
        
"""

import re

class Validator:
    def __init__(self):
        pass
    
    def phoneNumber(self , phoneNumber = ""):

        if re.match( r" (\(\+504\))?9\d{3}-?\d{4} " , phoneNumber ):
            return True

        return False

    def phoneNumbers(self,phoneNumbers = []):
        result = []
        for number in phoneNumbers:
            resultElement = [number,self.phoneNumber(number)]
            result.append(resultElement)
        return result
        




validator = Validator()

userPhoneNumber = "9213-8888"
print ("El numero de telefono %s es valido: %s" % (userPhoneNumber , validator.phoneNumber(userPhoneNumber)))


userPhoneNumbers = ["(+503)9111-1111", "(+503)91111111" , "(+50)9111-1111" , "91111111" , "9111-1111", "9111-1-111" , "91111-111"]

print (validator.phoneNumbers(userPhoneNumbers))

#(((([0-2]\d)|(3[0-1]))(\/|-)((1[02])|(0?[13578])))|((([0-2]\d)|(30))(\/|-)((11])|(0?[469])))|((([0-2]\d))(\/|-)(0?[2])))(\/|-)(\d\d\d\d)