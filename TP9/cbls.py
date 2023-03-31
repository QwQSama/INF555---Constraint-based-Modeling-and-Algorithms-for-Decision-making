"""Simple implementation to aid with (Constraint-Based) Local Search."""
from random import choice, choices
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt

Move = Tuple[int, int]
State = List[int]


class Board:
    """Represents an NxN board to put N queens on."""

    def __init__(self, n: int, random: bool = False):
        """Initialize the board."""
        self.n: int
        self.state: State

        self.n = n
        if random:
            self.state = choices(range(n), k=n)
        else:
            self.state = [0] * n

    def __str__(self) -> str:
        """Return a string for display."""
        return "\n".join(
            " ." * line + " #" + " ." * (self.n - line - 1) for line in self.state
        )

    def cost(self, move: Optional[Move] = None) -> int:
        """Compute the violation-cost for alldifferent constraints."""
        state = self.apply_move(move)
        stateplus, stateminus = zip(
            *((pos + i, pos - i) for i, pos in enumerate(state))
        )
        return (
            self.conflicts(state) + self.conflicts(list(stateplus)) + self.conflicts(list(stateminus))
        )

    @staticmethod
    def conflicts(assignment: List[int]) -> int:
        """Return the number of equalities in a given list of ints."""
        # return sum(map(lambda x: x * (x - 1) // 2, Counter(assignment).assignment()))
        count = 0
        increment = 1
        assignment.sort()
        last = assignment[0]
        for item in assignment[1:]:
            if item == last:
                count += increment
                increment += 1
            else:
                last = item
                increment = 1
        return count

    def neigborhood(self) -> List[Tuple[Move, int]]:
        """Generate all possible moves from the current position."""
        moves = []
        for i, pos in enumerate(self.state):
            moves.extend(
                [((i, n), self.cost((i, n))) for n in range(self.n) if n != pos]
            )
        return moves

    def show_all_costs(self) -> str:
        """Return a string with all costs."""
        current_cost = self.cost()
        return "\n".join(
            [
                " ".join(
                    [
                        f"{current_cost:2d}"
                        if column == self.state[line]
                        else f"{self.cost((line, column)):2d}"
                        for column in range(self.n)
                    ]
                )
                for line in range(self.n)
            ]
        )

    def plot_all_costs(self):
        """Use matplotlib to plot all costs."""
        cost = [
            [self.cost((line, column)) for column in range(self.n)]
            for line in range(self.n)
        ]
        fig, ax = plt.subplots()
        ax.imshow(cost, cmap=plt.cm.Oranges, vmin=0)
        for i in range(self.n):
            for j in range(self.n):
                ax.text(j, i, cost[i][j], ha="center", va="center")
        plt.show()

    def apply_move(self, move: Optional[Move]) -> State:
        """Apply a move to the current state."""
        new_state = self.state.copy()
        if move:
            new_state[move[0]] = move[1]
        return new_state


class LocalSearch:
    """Generic Local Search class for the N-Queens problem."""

    def __init__(self, n: int, random: bool = True, debug: bool = False, **kwargs):
        """Initialize a board."""
        self.board = Board(n, random)
        self.debug = debug

    def run(self) -> int:
        """From current board iterate local search until stopping criterion is met."""
        stop = False
        if self.debug:
            print(self.board.cost())
            print(self.board)
        while not stop:
            moves = self.board.neigborhood()
            move, cost, self.board.state, stop = self.select(moves)
            if self.debug:
                print(move, cost)
                print(self.board)
        return cost

    def select(
        self, moves: List[Tuple[Move, int]]
    ) -> Tuple[Optional[Move], int, State, bool]:
        """Select an optional move, return the corresponding cost and state.

        lastly return the stopping criterion's truth value
        """
        raise NotImplementedError

    @classmethod
    def evaluate(cls, n: int = 8, iterations: int = 100, **kwargs) -> float:
        """Evaluate the average cost after iterations runs of a searcher."""
        cost = 0
        for _i in range(iterations):
            instance = cls(n=n, random=True, **kwargs)
            cost += instance.run()
        return cost / iterations


class RandomWalk(LocalSearch):
    """Implement a random walk."""

    limit: int = 100

    def __init__(self, n: int, random: bool, **kwargs):
        """Initialize."""
        super().__init__(n, random, **kwargs)
        self.best = self.board.state
        self.cost = self.board.cost()
        self.counter = 0

    def select(
        self, moves: List[Tuple[Move, int]]
    ) -> Tuple[Optional[Move], int, State, bool]:
        """Select next move randomly."""
        move, cost = choice(moves)
        state = self.board.apply_move(move)
        if cost < self.cost:
            self.cost = cost
            self.best = state
        self.counter += 1
        if self.counter >= self.limit:
            return None, self.cost, self.best, True
        return move, cost, state, False


if __name__ == "__main__":
    print(RandomWalk.evaluate())
