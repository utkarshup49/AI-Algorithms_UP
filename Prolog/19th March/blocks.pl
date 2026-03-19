ontable(a).
ontable(c).

on(d, c).
on(b, a).
on(e, b).

heavy(b).
heavy(d).

clear(e).
clear(d).

wooden(b).

big(X) :- heavy(X), wooden(X).
blue(X) :- clear(X).
blue(X) :- wooden(X).

green(Y) :- on(X, Y), big(X), blue(X).
