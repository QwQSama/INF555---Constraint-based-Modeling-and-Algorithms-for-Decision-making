% Fourier's 1823 illustrative example for
% modeling and solving decision problems with inequalities over the reals

% Variables
var float: A; % pressures on the 3 legs of an isocele rectangle triangle table    
var float: B;
var float: C;

var float: X;        % position of the weight
var float: Y;

% Data
float: p;               % weight to place

float: xB;          % triangle table placed in A=(0,0) B=(xB,0) C=(0,yC)
float: yC; 

% Constraints

constraint 0<=A /\ A<=1;

constraint 0<=B /\ B<=1;

constraint 0<=C /\C <=1;

constraint A+B+C = p;

constraint p*X = xB*B;

constraint p*Y = yC*C;

% parametric objective function

float: a;
float: b;
float: c;
float: x;
float: y;
var float: f = a*A+b*B+c*C+x*X+y*Y;

solve minimize f;
