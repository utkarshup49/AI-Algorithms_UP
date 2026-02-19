start :-
    write('X= '), read(X),
    write('Y= '), read(Y),
    arith(X, Y).

arith(X, Y) :-
    add(X, Y),
    subt(X, Y),
    mult(X, Y),
    div(X, Y).

add(X, Y) :-
    R is X + Y,
    write('Add: '), writeln(R).

subt(X, Y) :-
    R is X - Y,
    write('Sub: '), writeln(R).

mult(X, Y) :-
    R is X * Y,
    write('Mul: '), writeln(R).

div(X, Y) :-
    Y =\= 0,
    R is X / Y,
    write('Div: '), writeln(R).

main :-
    X = 10,
    Y = 5,
    arith(X, Y).
