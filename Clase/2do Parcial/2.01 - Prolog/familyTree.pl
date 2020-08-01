/*
    Basics of Prolog
    @author swd
    @date 2020/07/30
    @version 0.1
*/

mujer('Gabriel').
mujer('Rosa Maria').

hombre('Alexis').
hombre('David').
hombre('Edgar').

progenitor/a('Alexis', 'Rosa Maria').
progenitor/a('Gabriel', 'Rosa Maria').
progenitor/a('Alexis', 'David').
progenitor/a('Gabriel', 'David').
progenitor/a('Alexis', 'Edgar').
progenitor/a('Gabriel', 'Edgar').

/*
    Para que alguien sea madre, tiene que ser progenitor/a y mujer.
    Para que alguien sea padre, tiene que ser progenitor/a y hombre.
    Para que alguien sea hermano/a, tiene que tener los mismos padres.

    ------
    Para que alguien sea hermano, tiene que tener los mismos padres y ser hombre.
    Para que alguien sea hermana, tiene que tener los mismos padres y ser mujer.
*/

madre(X, Y) :-
    progenitor/a(X,Y),
    mujer(X)

padre(X, Y) :-
    progenitor/a(X,Y),
    padre(X)

hermano/a(X, Y) :-
    madre(A, X),
    padre(B, X),
    padre(C, Y),
    madre(D, Y),

    A == C,
    B == D.





