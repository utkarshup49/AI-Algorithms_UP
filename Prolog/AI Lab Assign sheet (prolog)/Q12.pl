
gcd(M, N, G) :- N > M, gcd(N, M, G).

% Case 2: Base case - If N is 0, the GCD is M

gcd(M, 0, M).

% Case 3: If N > 0, find the remainder and recurse

gcd(M, N, G) :- 
    N > 0, 
    Rem is M mod N, 
    gcd(N, Rem, G).