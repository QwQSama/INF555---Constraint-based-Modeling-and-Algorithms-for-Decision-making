from enum import Enum
from typing import List, Set
Var = int
Literal = int
Clause = Set[Literal]
Instance = List[Clause]

Value = Enum('Value', ['Unassigned', 'True', 'False'])
Assignment = List[Value]


def unit_propagate(instance: Instance, assignment: Assignment) -> (Instance, Assignment):
    """Apply BCP to current instance and update assignment."""
    l_true = []
    l_false = []
    res = []
    for v in range(len(assignment)):
        if assignment[v] == "True":
            l_true.append(v+1)
        elif assignment[v] == "False":
            l_false.append(v+1)
        v += 1
    for c in instance:
        f_in = True
        lc = c.copy()
        for vp in l_true:
            if vp in c:
                f_in = False
            lc = lc - {vp, -vp}
        for vn in l_false:
            if -vn in c:
                f_in = False
            lc = lc - {vn, -vn}
        if f_in:
            res.append(lc)
    instance = res.copy()
    res = []
    l_unit = []
    for c in instance:
        if len(c) == 1:
            l_unit.append(list(c)[0])
    if len(l_unit) == 0:
        return instance, assignment

    for v in l_unit:
        if -v in l_unit:
            return [],assignment
    
    for v in l_unit:
        if v>0:
            assignment[v-1] = 'True'
        else:
            assignment[v-1] = 'False'
    

    return instance, assignment
