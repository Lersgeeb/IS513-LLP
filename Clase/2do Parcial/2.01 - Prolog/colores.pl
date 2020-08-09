/*
    Basics of Prolog
    @author swd
    @date 2020/07/30
    @version 0.1


% \== operador de distinto
% \+ operador de negación
%  "," and 
%  ";" or

*/

color(rojo).
color(verde).
color(azul).
color(amarillo).

rgb(X) :-
    X == rojo;
    X == verde;
    X == azul.
    