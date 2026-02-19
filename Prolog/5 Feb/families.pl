parent(ana, john).
parent(ana, pauline).
parent(john, ian).
parent(cathy, ian).
parent(ian, lucy).
parent(ian, peter).

female(ana).
female(pauline).
female(cathy).
female(lucy).

male(john).
male(ian).
male(peter).

mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
grandfather(X,Z):- parent(X,Y),parent(Y,Z),male(X).

children(X,Y):- parent(Y,X).
sibling(X,Z):- parent(Y,X),parent(Y,Z).
brother(X,Z):- parent(Y,X),parent(Y,Z),male(X).

main :-
    findall(X, parent(X, _), L),
    writeln(L).
