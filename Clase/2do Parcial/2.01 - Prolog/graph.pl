/*
    Basics of Prolog
    @author swd
    @date 2020/07/30
    @version 0.1
*/

% https://www.cpp.edu/~jrfisher/www/prolog_tutorial/2_15.html

% \== operador de distinto
% \+ operador de negación

%15, 7, 3, 2, 1, 0

% node1, node2 , distance
edges(0,1,1).
edges(1,5,1).
edges(1,2,1).
edges(2,6,1).
edges(2,3,1).

%  "," and 
%  ";" or

connected(X, Y) :-
    edges(X, Y, 1) ;
    edges(Y, X, 1).

path(A, B, Path) :-
    travel(A, B, [A], Q),
    reverse(Q, Path).


% [head, tail]

travel(A, B, P, [B|P]) :-
    connected(A, B).


travel(A, B, Visited, Path) :-
    connected(A, C).
    C \== B, 
    \+member(C, Visited),
    travel(C,B,[C|Visited],Path).
