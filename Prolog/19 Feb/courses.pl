% facts
easy(hardware).
easy(graphics).

not_easy(logic).

books_available(hardware).
books_available(database).

eight_credits(graphics).
lab(graphics).

takes(mary, compiler).

% rules
takes(_, Y) :-
    easy(Y),
    books_available(Y).

takes(_, Y) :-
    eight_credits(Y),
    lab(Y).
