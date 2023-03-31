include "ATC.mzn";

constraint forall (i in 2..nf) (precedes(i-1, i));

solve:: int_search(time, input_order, indomain_min, complete) minimize time[nf];