include "ATC.mzn";

array[1..nf] of var int: order;

constraint forall (i,j in 1..nf where i < j)
    (
        order[i] != order[j] /\
        order[i] <= nf /\
        order[i] >= 1
    );

constraint forall (i in 2..nf )
    (
        (time[order[i-1]] <time[order[i]] ) /\
        (precedes(order[i-1], order[i]))
    );


constraint forall (i in 1..nf )
    (
        (order[i] == i) \/
        (
            (expectedtime[i] > 300) /\
            expectedtime[order[i]] > 300 /\
            (
                ((expectedtime[i] > 1200) /\ (expectedtime[order[i]] > 1200)) \/
                (corridor[i] != corridor[order[i]])
            )
        )
    );


solve minimize max(time);