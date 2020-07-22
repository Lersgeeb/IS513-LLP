-- Author: its_anaehm
-- Description: Programa que calcule el factorial de un número 

WITH Ada.Text_io;
WITH Ada.Integer_text_io;
 
 
PROCEDURE Factorial IS
 --ENTRADA: Un número entero al cual se le desea calcular su factorial
 --PRECONDICIÓN: Números enteros
 --SALIDA: Un número entero equivalente al valor del factorial,
 --POSTCONDICIÓN: n*factorial(n-1)

   USE Ada.Text_io;
   USE Ada.Integer_Text_io;
 
   NUMERO:Integer;

FUNCTION factorial( num: IN integer) RETURN integer IS
 
BEGIN
   IF num=0 OR num=1 THEN
      RETURN 1;
   ELSE
   RETURN ( num * factorial(num-1) );
   END IF; 
END factorial;
 
 
BEGIN 
 put("Introduzca el numero al que le desea calcular su factorial: ");
 get(numero);
 new_line;
 put("El factorial de "); put(numero,width=>1); put(" es "); put( factorial(numero), width=>1); new_line;
END Factorial;