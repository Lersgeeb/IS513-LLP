:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
server(Port) :-
    http_server(http_dispatch, [port(Port)]).

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

