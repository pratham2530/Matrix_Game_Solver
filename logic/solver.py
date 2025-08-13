"""
This module solves two-player zero-sum games by formulating them as linear programs
and using the Pyomo optimization library. It finds the optimal mixed strategies
and the value of the game.
"""

from typing import Tuple

import numpy as np
from pyomo.environ import (ConcreteModel, Constraint, NonNegativeReals,
                           Objective, SolverFactory, Var, maximize)


def solve_game(payoff_matrix: np.ndarray) -> Tuple[float, ...]:
    """
    Compute optimal strategies and game value for a zero-sum matrix game.

    Args:
        payoff_matrix: 2D numpy array where payoff_matrix[i,j] represents
                     the payoff when row player uses strategy i and column
                     player uses strategy j.

    Returns:
        Tuple containing:
        - game_value (float): The value of the game
        - strategy_weights (tuple): Probability distribution over row player's strategies

    Example:
        >>> import numpy as np
        >>> matrix = np.array([[3, -2], [-1, 4]])
        >>> solution = solve_game(matrix)
        >>> print(f"Game value: {solution[0]}")
        >>> print(f"Strategy: {solution[1:]}")
    """
    rows = payoff_matrix.shape[0]
    model = ConcreteModel()

    # Decision variables
    model.x = Var(range(rows), within=NonNegativeReals)
    model.v = Var()

    # Objective: Maximize the game value
    model.obj = Objective(expr=model.v, sense=maximize)

    # Constraints
    def payoff_constraint(mdl, j):
        return sum(payoff_matrix[i, j] * mdl.x[i] for i in range(rows)) >= mdl.v

    model.matrix_cons = Constraint(
        range(payoff_matrix.shape[1]), rule=payoff_constraint
    )
    model.prob_cons = Constraint(expr=sum(model.x[i] for i in range(rows)) == 1)

    # Solve
    SolverFactory("glpk").solve(model)

    # Extract solution
    return (round(model.v(), 3),) + tuple(round(model.x[i](), 3) for i in range(rows))
