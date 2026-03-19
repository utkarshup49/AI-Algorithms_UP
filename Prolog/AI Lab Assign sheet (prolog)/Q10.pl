% Base case: factorial of 0 is 1.
factorial(0, 1).

% Recursive rule:
factorial(N, F) :-
    N > 0,               % Ensure N is positive
    N1 is N - 1,         % Decrement N
    factorial(N1, F1),   % Recursive call to find (N-1)!
    F is N * F1.         % Multiply N by the result of (N-1)!