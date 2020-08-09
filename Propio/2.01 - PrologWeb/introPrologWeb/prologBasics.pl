my_handler_code() :-
    write('Defecto').

my_handler_code(X):-
    X == opcion1,
    write("Escribir opcion 1").


my_handler_code(X):-
    X == opcion1(extra),
    write("Escribir opcion 1 con extras funcionalidades").

