int: nf;
int: nc;

set of int: CAT = 1..3;
set of int: COR = 1..nc;

array[1..nf] of int: expectedtime;
array[1..nf] of CAT: category;
array[1..nf] of COR: corridor;

array[CAT, CAT] of int: distance_matrix = [|100, 130, 160,
                                           |70, 80, 100,
                                           |60, 60, 70|];
array[1..nf] of var int: time;

constraint forall (i in 1..nf) 
    (
        (time[i] > 0.8 * expectedtime[i]) /\ 
        (time[i] < 3 * expectedtime[i])
    );

predicate precedes(var int: i, var int: j) = 
    (
        (time[j] - time[i]) > (distance_matrix[category[i], category[j]]) /\
        time[i] < time[j]
    );