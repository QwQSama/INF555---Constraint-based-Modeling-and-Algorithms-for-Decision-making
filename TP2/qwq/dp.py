# These are Python3 type-annotations
from typing import List, Set
Var = int
Literal = int
Clause = Set[Literal]
Instance = List[Clause]


def davis_putnam(instance: Instance, var: Var) -> Instance:
    """Eliminate var from instance using Davis-Putnam algorithm."""
    L_no_x = []
    L_xp = [] 
    L_xn = []
    for c in instance:
        if var in c:
            L_xp.append(c - {var})
        elif -var in c:
            L_xn.append(c - {-var})
        else:
            L_no_x.append(c)
    instance = []
    for c in L_no_x:
        instance.append(c)
    
    for cp in L_xp:
        for cn in L_xn:
            instance.append(cp | cn)


    return instance
