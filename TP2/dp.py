# These are Python3 type-annotations
from typing import List, Set
Var = int
Literal = int
Clause = Set[Literal]
Instance = List[Clause]


def davis_putnam(instance: Instance, var: Var) -> Instance:
    """Eliminate var from instance using Davis-Putnam algorithm."""
    return instance
