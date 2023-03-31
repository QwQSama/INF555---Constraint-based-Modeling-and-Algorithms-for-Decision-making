include "ATC.mzn";

constraint forall (i in 2..nf) (precedes(i-1, i));

solve minimize time[nf];
