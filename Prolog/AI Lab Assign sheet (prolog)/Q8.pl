easy_course(hardware).
books_available(hardware).
easy_course(graphics).
credits(graphics,8).
has_lab(graphics).
books_available(database).

takes(mary,compiler).

takes(X,Y) :- easy_course(Y), books_available(Y).

takes(X,Y) :- credits(Y,8), has_lab(Y).