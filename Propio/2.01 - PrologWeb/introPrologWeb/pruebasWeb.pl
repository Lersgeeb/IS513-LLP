:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_error)).
:- use_module(library(http/html_write)).
- use_module(library(http/http_files)).
:- use_module(library(http/http_path)).
:- encoding(utf8).

:- multifile http:location/3.
:- dynamic   http:location/3.


server(Port) :-
    http_server(http_dispatch, [port(Port)]).



%Rutas
:- http_handler(root(.), index , []).
:- http_handler(root(.), index , []).
:- http_handler(root('htmldoc'), handlerFunction(htmldoc), []).



handlerFunction(WhatToSay, Request) :-
    isHtmlDoc(WhatToSay, Request).

isHtmlDoc(WhatToSay, Request):-
    WhatToSay == htmldoc,
    reply_html_page(
	   	[
			title('Mi Título'),
            link([rel='stylesheet', href='/style/style.css'])
		],
		[\page_content(Request)]).

page_content(_Request) -->
	html(
        div(
            [class='mainTextClass'],
	        [
                h1('Esto es el Encabezado de la Página'),
                p('Soy un Párrafo'),
                p(['Soy otro Párrafo pero con ', b('Negrita!'), &(copy)]),
                p([style='font-size: 36pt', title='tooltip text'],'Soy otro Párrafo pero con Estiloo '),
                img(src='/images/ejemplo.png'),
                img(src='/images/encoding.png'),
                \some_included_stuff,
                \more_included_stuff('Whoop Whoop!'),
                a([href='http:example.com?foo=' + encode('some value with & illegal chars')], 'a link'),
                pre(code('Probando code')),
                p(class=[someclass, someotherclass], ['this has class', b('y negrita')]),
                \code_txt('print( "Hello World" )')
	        ]
        )
    ).

some_included_stuff -->
	html([p('Some included stuff')]).

more_included_stuff(X) -->
	html([p(['More included stuff: ', b(X)])]).


code_txt(X) -->
	html(
       pre(
           [class = 'codetxtClass'],
           [code(X)]
       )
    ).

index(_Request) :-
    format('Content-type: text/plain~n~n'),
    format('Hello World!~n').



%Rutas de Imagenes
http:location(images, root(images), []).
user:file_search_path(imgs, './imgs').

:- http_handler(images('ejemplo.png'), ejemplo, []).
ejemplo(Request) :-
    http_reply_file(imgs('ejemplo.png'),[unsafe(true)],Request).

:- http_handler(images('encoding.png'), encoding, []).
encoding(Request) :-
    http_reply_file(imgs('encoding.png'),[unsafe(true)],Request).

%Ruta para estilos agregados.
http:location(style, root(style), []).
user:file_search_path(fileStyle, './style').

:- http_handler(style('style.css'), style, []).
style(Request) :-
    http_reply_file(fileStyle('style.css'),[unsafe(true)],Request).

/* Iniciar Servidor de Prolog en el Puerto 8080
:- initialization
    http_server(http_dispatch, [port(8080)]).
*/