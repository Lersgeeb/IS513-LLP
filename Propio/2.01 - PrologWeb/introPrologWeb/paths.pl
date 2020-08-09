:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).

server(Port) :-
    http_server(http_dispatch, [port(Port)]).

%
%  Add another abstract base location like root
%  this one is files, and we map it to /f,
%  so /f/limburger can be described as files(limburger)
:- multifile http:location/3.
:- dynamic   http:location/3.

http:location(files, '/f', []).


user:file_search_path(nombre, './nombre').
user:file_search_path(completo, nombre(completo)).


:- http_handler(root(.), index , []).
:- http_handler(root('nombre'), handlerFunction(nombre), []).
:- http_handler(root('nombre/completo'), handlerFunction(completo), []).

handlerFunction(WhatToSay, _Request) :-
    isName(WhatToSay);
    isFullName(WhatToSay).
        
isName(WhatToSay):-
    WhatToSay == nombre,
    format('Content-type: text/plain~n~n'),
    format('Hola me llamo Gabriel!~n').

isFullName(WhatToSay):-
    WhatToSay == completo,
    format('Content-type: text/plain~n~n'),
    format('Hola me llamo Gabriel Enrique Escobar banegas!~n').

index(_Request) :-
    format('Content-type: text/plain~n~n'),
    format('Hello World!~n').

