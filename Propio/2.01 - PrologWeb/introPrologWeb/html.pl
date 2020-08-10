:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_error)).
:- use_module(library(http/html_write)).
:- encoding(utf8).

server(Port) :-
    http_server(http_dispatch, [port(Port)]).


:- http_handler(root(.), index , []).

index(Request):-
    reply_html_page(
	   	[title('Mi Título')],
		[\page_content(Request)]
	).

page_content(_Request) -->
	html(
	   [
			h1('Esto es el Encabezado de la Página'),
			p('Soy un Párrafo'),
			p(['Soy otro Párrafo pero con ', b('Negrita!'), &(copy)]),
			p([style='font-size: 36pt', class='styleText'],'Soy otro Párrafo pero con Estilo'),
			\some_included_stuff,
	    	\more_included_stuff('Whoop Whoop!'),
	   ]
	).

some_included_stuff -->
	html([p('Some included stuff')]).

more_included_stuff(X) -->
	html([p(['More included stuff: ', b(X)])]).


