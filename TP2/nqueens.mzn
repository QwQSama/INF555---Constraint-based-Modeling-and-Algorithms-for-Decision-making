int: n;
array[1..n] of var 1..n: queens;

constraint forall (i, j in 1..n where i < j) (
   queens[i] != queens[j] /\
   queens[i] != queens[j] + j - i /\
   queens[i] != queens[j] + i - j
);

solve satisfy;

output [if fix(queens[j]) == i then "Q" else "." endif ++
        if j == n then "\n" else " " endif | i,j in 1..n]
