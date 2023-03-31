
include "ATC.mzn";


predicate pd(var int: i, var int: j) = 
    (
        (expectedtime[i] > 300) /\
        (expectedtime[j] > 300) /\
        (
            ((expectedtime[i]  > 1200) /\ (expectedtime[j] > 1200))\/
            (corridor[i] != corridor[j])
        )
    );

constraint forall (i,j in 1..nf where i < j)
    (
        if (time[i] > time[j])
        then
            (pd(i,j))/\
            (precedes(j,i))
        else
            (precedes(i,j))
        endif
    );


solve minimize max(time);