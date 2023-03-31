int: nc;
enum Vertices;
set of int: NbEdges;
array[NbEdges] of Vertices: Edges1;
array[NbEdges] of Vertices: Edges2;

array[Vertices,1..nc] of var bool: Color;
constraint 
    forall (v in Vertices)
    (
        exists(i in 1..nc) (Color[v,i])
    );
constraint 
    forall (ei in NbEdges)
    (
        forall(i in 1..nc) (not (Color[Edges1[ei],i] /\ Color[Edges2[ei],i]) )
    );


solve satisfy;
