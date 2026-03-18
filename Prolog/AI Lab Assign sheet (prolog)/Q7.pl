fruit(apple).
cooked(apple).
fruit(mango).

tasty(X) :- fruit(X), \+ cooked(X).