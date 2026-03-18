% --- Physical Facts (from the table) ---
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

% --- Logical Rules (from Other Information) ---

% 1. Every big blue block is on a green block.
on(X, green_block) :- big(X), blue(X).

% 2. Each heavy, wooden block is big.
big(X) :- heavy(X), wooden(X).

% 3. All blocks with clear tops are blue.
blue(X) :- clear(X).

% 4. All wooden blocks are blue.
blue(X) :- wooden(X).