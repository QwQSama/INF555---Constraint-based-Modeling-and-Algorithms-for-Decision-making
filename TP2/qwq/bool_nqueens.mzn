int: n;
array[1..n,1..n] of var bool: queens;

constraint 
    forall (i in 1..n) 
    (
        exists(j in 1..n) (queens[i,j])
    );

constraint 
    forall (i in 1..n) 
    (
        exists(j in 1..n) (queens[j,i])
    );

constraint 
    forall (i in 1..n) 
    (
        forall(j,k in 1..n where j!=k) 
            (not (queens[i,j] /\ queens[i,k]))
    );

constraint 
    forall (i in 1..n) 
    (
        forall(j,k in 1..n where j!=k) 
            (not (queens[j,i] /\ queens[k,i]))
    );

constraint 
    forall (i,j in 1..n) 
    (
        forall(k in 1..n) 
            ((not (queens[i,j] /\ queens[i+k,j+k])) /\ (not (queens[i,j] /\ queens[i-k,j+k])))
    );

solve satisfy;

output [if fix(queens[i,j]) then "Q" else "." endif ++
        if j == n then "\n" else " " endif | i,j in 1..n]