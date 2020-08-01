/*
    Basics of Prolog
    @author swd
    @date 2020/07/30
    @version 0.1
*/

factorial(0 , 1).
factorial(N, Respuesta):-
    N > 0,
    Nmenos1 is N-1,
    factorial(Nmenos1, RespuestaNmenos1),
    Respuesta is RespuestaNmenos1 * N.