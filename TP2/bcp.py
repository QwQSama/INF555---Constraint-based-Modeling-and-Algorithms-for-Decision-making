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
    return instance, assignment
