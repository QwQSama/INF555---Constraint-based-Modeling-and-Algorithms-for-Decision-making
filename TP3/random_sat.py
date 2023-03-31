import time
from typing import List, Set
import inf555

Var = int
Literal = int
Clause = Set[Literal]
Instance = List[Clause]


def literal_to_minizinc(lit: Literal) -> str:
    return ('not ' if lit < 0 else '') + f'vars[{str(abs(lit))}]'


def clause_to_minizinc(clause: Clause) -> str:
    return 'constraint ' + ' \\/ '.join(map(literal_to_minizinc, clause)) + ';'


def time_and_result(instance: Instance, solver=inf555.chuffed) -> (float, bool):
    '''send an instance to MiniZinc, time the execution.

    also return the satisfiability as a boolean'''
    # we consider that the highest variable appearing is our number of
    # variables
    nvar = max([abs(lit) for clause in instance for lit in clause])
    with open('sat.mzn', 'w') as f:
        print(f'array[1..{nvar}] of var bool: vars;', file=f)

        for clause in instance:
            print(clause_to_minizinc(clause), file=f)

    # get time from solutions.log instead?
    start = time.perf_counter()
    solution = inf555.minizinc('sat.mzn', solver=solver)
    stop = time.perf_counter()

    return stop - start, (solution.status != inf555.Status.UNSATISFIABLE)
