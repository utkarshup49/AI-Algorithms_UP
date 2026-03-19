delicious(cake).
delicious(pickles).
delicious(biryani).
spicy(pickles).

likes(priya,coffee).

likes(priya,Food) :- delicious(Food).

likes(prakash,Food) :- delicious(Food), spicy(Food).

