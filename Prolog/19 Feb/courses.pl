% facts
easy(hardware).
easy(graphics).
student(mary).

not_easy(logic).

books_available(hardware).
books_available(database).

eight_credits(graphics).
lab(graphics).

takes(mary, compiler).


takes(X, Y) :-
    student(X),
    easy(Y),
    books_available(Y).

takes(X, Y) :-
    student(X),
    eight_credits(Y),
    lab(Y).
    
% Tests:
% Does Mary take graphics?
% takes(mary, graphics)
% Output: true

% Which course does Mary take?
% takes(mary, C)
% Output:
% C = compiler
% C = hardware
% C = graphics

% Who takes graphics?
% takes(X, graphics)
% Output:
% X = mary
