easy(hardware).

easy(graphics).

not_easy(logic).

books_available(hardware).
books_available(database).

credits(graphics, 8).
lab(graphics).

takes(mary, compiler).

takes(X, Y) :-
    easy(Y),
    books_available(Y).

takes(X, Y) :-
    credits(Y, 8),
    lab(Y).

main :-
    % 1) Does Mary take graphics?
    (takes(mary, graphics) ->
        writeln('Yes, Mary takes graphics.');
        writeln('No, Mary does not take graphics.')
    ),

    % 2) Which course does Mary take?
    writeln('Courses Mary takes:'),
    forall(takes(mary, C),
           writeln(C)),

    % 3) Who takes graphics?
    writeln('Students who take graphics:'),
    forall(takes(S, graphics),
           writeln(S)).
