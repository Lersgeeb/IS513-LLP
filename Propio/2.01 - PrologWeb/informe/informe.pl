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

%Ruta por defecto (Index)
index(Request) :-
   reply_html_page(
	   	[
			title('Informe Prolog'),
            link([rel='stylesheet', href='/style/style.css'])
		],
		[\page_content(Request)]
    ).
    

page_content(_Request) -->
	html(
        div(
            [class='mainDivClass'],
            div(
                [class='mainTextClass'],
                [
                    div(
                        [class='imgTitle'],
                        [img(src='/images/prolog.png')]
                    ),
                    h1('Información del autor'),
                    \infostudent('Universidad:','Universidad Nacional Autónoma de Honduras'),
                    \infostudent('Estudiante:','Gabriel Enrique Escobar Banegas'),
                    \infostudent('Asignatura:','Lenguajes de Programación'),
                    \infostudent('Catedrático:','José Manuel Inestroza'),
                    \infostudent('Correo:','geescobar@unah.hn'),
                    \infostudent('Fecha:','10/08/2020'),
                    h1('Prolog un Lenguaje de Programación.'),
                    p(['Prolog es un lenguaje de programación que está orientada a la programación lógica. Su estructura se basa en
                    dos principales elemento, hechos y clausulas. Las clausulas son proposiciones que pueden ser determinadas como 
                    falsas o verdaderas de acuerdo a un conjunto de hechos establecidos. En términos más simples prolog es un sistema 
                    al cual se alimenta de información que pueden ser reglas, procedimientos o hechos. Todas las relaciones que encuentra
                    luego son utilizadas para resolver alguna consulta formulada por el usuario.']),
                    h2('Uso de prolog'),
                    p([
                        'Prolog también ofrece herramientas que incluyen el “Backtracking” (retroceso). El Backtracking es una característica 
                        que se basa en determinar un objetivo y retroceder buscando los hechos que sean necesarios para lograr cumplirla. 
                        Esto puede ser empleado al momento de encontrar una falla en alguna tarea. Esta característica única ha sido muy útil 
                        en campos como la inteligencia artificial.'
                    ]),
                    p([
                        'Otra función con la que cuenta prolog son las consultas. Una consulta se basa en la entrada de una proposición la cual 
                        contiene hechos que pueden ser variados y prolog se encarga de retornar todos aquellos hechos que hacen la proposición 
                        verdadera. Por esta misma característica es por la cual Prolog también puede ser empleada como un lenguaje para la 
                        manipulación de base de datos.'
                    ]),
                    h2('Introducción a Prolog'),
                    p([
                        'La sintaxis es una pieza fundamental el cual forma parte de cualquier lenguaje de programación. Este es un elemento 
                        que puede cambiar dependiendo de las reglas que establezca el lenguaje. Muchas veces el programador no encontrara gran
                        desafío al adaptarse a una nueva sintaxis, esto es debido a que a pesar de ser diferentes presentan un enfoque similar
                        al momento de cómo resolver un problema.  Sin embargo los lenguajes orientados a una programación lógica no cumplen 
                        con esta misma relación.  Un ejemplo de ello es Prolog. El cual trabaja bajo un enfoque especial. El cual no consiste
                        en “Como” resolver un problema sino en segmentarlo y reducirlo a proposiciones que pueden ser determinadas como 
                        verdaderas o falsas y luego relacionarlas para generar estructuras más complejas.'
                    ]),
                    p([
                        'La sintaxis de Prolog trabaja con dos principales elementos, variables y constantes. Mediante estos elementos se pueden
                        construir hechos y clausulas. Para una clara comprensión primero es importante definir algunos elementos básicos del 
                        lenguaje el cual ayudara a manipular o elaborar estos dos elementos.'
                    ]),
                    \code_txt(\codeIntro),
                    p([style='font-size: 36pt', title='tooltip text'],'Soy otro Párrafo pero con Estiloo '),
                    img(src='/images/ejemplo.png'),
                    img(src='/images/encoding.png'),

                    a([href='http:example.com?foo=' + encode('some value with & illegal chars')], 'a link'),
                    pre(code('Probando code')),
                    p(class=[someclass, someotherclass], ['this has class', b('y negrita')]),
                    \code_txt('print( "Hello World" )'),
                    div([class='END'],[])
                ]
            )
        )
    ).

%Rutas de Imagenes
http:location(images, root(images), []).
user:file_search_path(imgs, './imgs').

:- http_handler(images('ejemplo.png'), ejemplo, []).
ejemplo(Request) :-
    http_reply_file(imgs('ejemplo.png'),[unsafe(true)],Request).

:- http_handler(images('encoding.png'), encoding, []).
encoding(Request) :-
    http_reply_file(imgs('encoding.png'),[unsafe(true)],Request).

:- http_handler(images('prolog.png'), prolog, []).
prolog(Request) :-
    http_reply_file(imgs('prolog.png'),[unsafe(true)],Request).

:- http_handler('/favicon.ico', icon, []).
icon(Request) :-
    http_reply_file(imgs('prolog.ico'),[unsafe(true)],Request).

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


%Funciones para la creacionde HTML

code_txt(X) -->
	html(
       pre(
           [class = 'codetxtClass'],
           [code(X)]
       )
    ).

infostudent(X,Y) -->
    html(
        p(
            [class='presentationStudent'],
            [b(X), ' ', Y]
        )
    ).


codeIntro() -->
html(
'/*
    Los siguientes son algunos de elementos del lenguaje de prolog más 
    comunes y a partir de ellos se pueden construir estructuras basadas 
    en proposiciones complejas.
*/

%   :-    ---     Implicación (de derecha a izquierda)
%   .     ---     Significa el final de la proposición 
%   ==    ---     Operador de igualdad
%   \\==   ---     Operador de distinto
%   \\+    ---     Operador de negación
%   ,     ---     Operador AND
%   ;     ---     Operador OR'
).