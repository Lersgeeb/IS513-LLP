:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_error)).
:- use_module(library(http/html_write)).
- use_module(library(http/http_files)).
:- use_module(library(http/http_path)).
:- encoding(utf8).


:- http_handler(root(.), http_reply_from_files('.', []), [prefix]).

:- initialization
    http_server(http_dispatch, [port(8080)]).

:- multifile http:location/3.
:- dynamic   http:location/3.


:- http_handler(root(.), index , []).
:- http_handler(root('htmldoc'), handlerFunction(htmldoc), []).



handlerFunction(WhatToSay, Request) :-
    isHtmlDoc(WhatToSay, Request).

isHtmlDoc(WhatToSay, Request):-
    WhatToSay == htmldoc,
    reply_html_page(
	   	[
			title('Mi Título')
		],
		[\page_content(Request)]).

page_content(_Request) -->
	html(
	   [
			h1('Esto es el Encabezado de la Página'),
			p('Soy un Párrafo'),
			p(['Soy otro Párrafo pero con ', b('Negrita!'), &(copy)]),
			p([style='font-size: 36pt', title='tooltip text'],'Soy otro Párrafo pero con Estiloo '),
            img(src='f/xd.png'),
			\some_included_stuff,
	    	\more_included_stuff('Whoop Whoop!'),
			a([href='http:example.com?foo=' + encode('some value with & illegal chars')],
            'a link')
	   ]
	).

some_included_stuff -->
	html([p('Some included stuff')]).

more_included_stuff(X) -->
	html([p(['More included stuff: ', b(X)])]).

index(_Request) :-
    format('Content-type: text/plain~n~n'),
    format('Hello World!~n').


%static(Request) :-
%    html([img(http_reply_file(files('xd.png'),[unsafe(true)],Request))]).
%server(8080).
