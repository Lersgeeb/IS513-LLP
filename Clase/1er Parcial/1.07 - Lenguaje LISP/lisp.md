PAC II 2020 - LLP 1100
@author swd
@date 2020/07/22
@version 0.1

LISP
=====

* Es un lenguaje de propósito general.
* Integers, Ratios, Complex Numbers, String, Arrays, Vector, Hash Tables, Funcions Streams.
* Expresiones-S se definen , recursivamentem como: 
    * Un tipo de dato simple, el cual se llama "átomo".
        * Un átomo corresponde con: número lista, cadenas de caracteres y símbolos.
    * Una lista de expresiones-S donde una expresion-S podría ser una lista de expresiones-S. que a su vez 
    podríaser listas, y se pueden obtener expresiones anidads de cualquier nivel de profunidad.

Expresión-S (S-expression)
-------

* Expresion Simbólica: es una notación de forma de texto usada en la representación de estructuras de árbol, está basda en listas anidadas, en donde cada sublista 
es un subárbol. Las expresiones_S se usan en la familia de lenguajes de programacion LISP. Su representación es mediante secuencias de cadenas de caracteres, delimitadas por paréntesis, y separadas por espacios: (= 4 (+ 2 2)). En C este ejemplo sería: 4== 2 + 2 .

Common LISP
------

* https://lisp-lang.org/
* Requiere el uso de notación pre-fija.
* En Consola lo ejecutaremos usando un programa SBCL (sudo aptitude).
    * http://www.sblc.org
    * http://www.sblc.org/manual

* Ejemplos:

    #
        (+ 1 2)
        (+ 1 (+ 1 1))
        (* (+ 1 2) (- 3 4)) ;Observe que existen espacios que separan cada elemento de la instrucción 
        (+ (+ 3 4) (+ (+ 4 5) 6))
        (+ 3 4 5 6) ; La función de adición puede tomar más de un parámetro.
       
        (defun funcion (x y) (+ x y 5)) ;Definición de una función
        (funcion 1 2) ; La ejecución de una función

        (let ((x 10)) x)
        (let ((y 10)) (- y 10))
        (list 4 5 6)
    #

* Para ejecutar un script:
    #
    $ sbcl --script program.lisp
    #

*  Tome en cuenta que:
    * Set que puede establecer el valor de Símbolos.
    * SetQ que puede establecer el valor de Variables.
    * SetF es un macro, posee la capacidad de definir 
    varios elementosL símbolos, variables, elementos 
    de un arreglo, instancias, etc.

* Ejemplo de petición de datos
    #
        (write (+ 1 (read)))
    #

* Ejemplo (sin imprimir resultado):
    #
        (defvar *variableCualquiera*)
        (setf *unavariableCualquiera* 42.1)
        (* 2.1 *unavariableCualquiera*)
    #

* Ejemplo de función y ejecución de función
    #
        ; se define una función
        (defun square (x) (* x x))

        ; se usa la función
        (write (square 3))
    #

* Ejercicio de un programa que imprime mensajes en pantalla y recibe datos del usuario
    #
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        : Ejemplo de programa en commn Lisp
        ; Usando SBCL
        ; @author swd
        ; @date 2020/07/22
        ; @version 0.1
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

        ; Mesnaje de bienvenida
        (write-line "")
        (write-line "")
        (write-line "Escriba en pantalla un dato numérico: ")
        (write-line "")

        ; Definir una variable y se solicita el dato al usuario
        (defvar *unaVariableCualquiera*)
        (setf *unaVariableCualquiera* (read))
        (write-line "")

        ;Se imprimen los resultados de una operación cualquiera
        (write-line "El resultado de su número * por 5 es: ")
        (write (* 5 *unaVariableCualquiera*))
        (write-line "")
    #

* Ejericio de factorial que imprime el resultado en pantalla de un número fijo.
    #
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ; Factorial usando Common lISp en SBCL
        ; @author swd
        ; @date 2020/07/22
        ; @version 0.1
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

        (deffun factorial (n) (
            if(< n 2) 1 (* n (factorial(- n 1)))
        ))

        (write (factorial 5))
    #