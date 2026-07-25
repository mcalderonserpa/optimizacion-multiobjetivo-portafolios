import numpy as np

from scipy.optimize import minimize

from src.metrics import (
    annual_return,
    annual_risk,
    sharpe_ratio
)

def objective(
    weights,
    covariance_matrix
):
    """
    Función objetivo del modelo ε-Constraint.

    Minimiza el riesgo anual del portafolio.
    """

    return annual_risk(
        weights,
        covariance_matrix
    )

def build_constraints(
    expected_returns,
    target_return
):

    return (

        {
            "type": "eq",
            "fun": lambda w: np.sum(w) - 1
        },

        {
            "type": "ineq",
            "fun": lambda w:
                annual_return(
                    w,
                    expected_returns
                ) - target_return
        }

    )

def optimize(
    expected_returns,
    covariance_matrix,
    n_points=100,
    risk_free_rate=0.0
):
    """
    Optimiza un portafolio mediante el método ε-Constraint.
    """

    n_assets = len(expected_returns)

    initial_weights = np.ones(n_assets) / n_assets

    bounds = tuple((0, 1) for _ in range(n_assets))

    target_returns = np.linspace(
        expected_returns.min(),
        expected_returns.max(),
        n_points
    )

    portfolio_returns = []
    portfolio_risks = []
    sharpe_ratios = []
    portfolio_weights = []

    for target_return in target_returns:

        constraints = build_constraints(
            expected_returns,
            target_return
        )

        result = minimize(
            objective,
            x0=initial_weights,
            args=(covariance_matrix,),
            method="SLSQP",
            bounds=bounds,
            constraints=constraints
        )

        if result.success:

            weights = result.x

            portfolio_return = annual_return(
                weights,
                expected_returns
            )

            portfolio_risk = annual_risk(
                weights,
                covariance_matrix
            )

            sharpe = sharpe_ratio(
                portfolio_return,
                portfolio_risk,
                risk_free_rate
            )

            portfolio_returns.append(portfolio_return)
            portfolio_risks.append(portfolio_risk)
            sharpe_ratios.append(sharpe)
            portfolio_weights.append(weights)

    portfolio_returns = np.array(portfolio_returns)
    portfolio_risks = np.array(portfolio_risks)
    sharpe_ratios = np.array(sharpe_ratios)
    portfolio_weights = np.array(portfolio_weights)

    best_index = np.argmax(sharpe_ratios)
    minimum_risk_index = np.argmin(portfolio_risks)

    best_portfolio = {
        "weights": portfolio_weights[best_index],
        "return": portfolio_returns[best_index],
        "risk": portfolio_risks[best_index],
        "sharpe": sharpe_ratios[best_index]
    }

    minimum_risk_portfolio = {
        "weights": portfolio_weights[minimum_risk_index],
        "return": portfolio_returns[minimum_risk_index],
        "risk": portfolio_risks[minimum_risk_index],
        "sharpe": sharpe_ratios[minimum_risk_index]
    }

    return {
        "returns": portfolio_returns,
        "risks": portfolio_risks,
        "sharpes": sharpe_ratios,
        "weights": portfolio_weights,
        "best_portfolio": best_portfolio,
        "minimum_risk_portfolio": minimum_risk_portfolio
    }