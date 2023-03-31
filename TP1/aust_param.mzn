enum Vertices;
set of int: NbEdges;
array[NbEdges] of Vertices: Edges1;
array[NbEdges] of Vertices: Edges2;

var int: max;
int: nc = 10;

set of int: num_color = 1..nc; 
array[Vertices] of var num_color: color;

constraint forall(i in NbEdges) (color[Edges1[i]] != color[Edges2[i]]);
constraint max >= max(i in Vertices)(color[i]);

solve minimize max;