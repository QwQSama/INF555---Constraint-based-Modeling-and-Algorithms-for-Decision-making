% parameter
int: D;              % duration in quarters
% variables
var float: R;        % quarterly repayment
var float: P;        % principal initially borrowed
var 0.0 .. 10.0: I;  % interest rate
var float: B;        % balance owing at end

% remember that you can use
% if/then/else/endif
% it is also possible to declare local variables like
% let { var float: b; } in
predicate cumulative_interest(
   var float: balance, var float: principal, var float: interest,
   var float: repayment, int: nbquarters) = 
      (
         if (balance ==0 /\ nbquarters > 0)
         then 
            cumulative_interest(
               principal, principal,
               interest, repayment, nbquarters
               )
         else
            cumulative_interest(
               (principal * (1 + interest) - repayment), (principal * (1 + interest) - repayment),
               interest, repayment, (nbquarters-1)
               )
         endif
      );

constraint cumulative_interest(B, P, I, R, D);

solve satisfy;

output [
   "Borrowing ", show_float(0, 2, P), " at ", show(I*100.0), 
   "% interest, and repaying ", show_float(0, 2, R), 
   "\nper quarter for ", show(D), " quarters, leaves ",
   show_float(0, 2, B), " owing\n"
];
