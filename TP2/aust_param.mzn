int: nc;
enum Vertices;
set of int: NbEdges;
array[NbEdges] of Vertices: Edges1;
array[NbEdges] of Vertices: Edges2;

array[Vertices] of var int: Color;
constraint forall (color in Color)(color >=0 /\ color < nc);
constraint forall (n in NbEdges)(Color[Edges1[n]] != Color[Edges2[n]]);

solve satisfy;
