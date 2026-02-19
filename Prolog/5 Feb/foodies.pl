delicious(cakes).
delicious(pickles).
delicious(biryani).

spicy(pickles).

likes(priya, coffee).

likes(priya, Y) :-
    delicious(Y).

likes(prakash, Y) :-
    delicious(Y),
    spicy(Y).

main :-
    findall(Y, likes(priya, Y), PriyaLikes),
    write('Priya likes: '), writeln(PriyaLikes),

    findall(Y, likes(prakash, Y), PrakashLikes),
    write('Prakash likes: '), writeln(PrakashLikes).
