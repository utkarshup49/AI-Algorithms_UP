% Rule 1: X is the max if X is greater than or equal to Y.
max_of_two(X, Y, X) :- X >= Y.

% Rule 2: Y is the max if Y is greater than X.
max_of_two(X, Y, Y) :- Y > X.