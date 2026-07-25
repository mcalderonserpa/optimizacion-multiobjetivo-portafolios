import numpy as np

from scipy.optimize import minimize

from src.metrics import (
    annual_return,
    annual_risk,
    sharpe_ratio
)

def objective(
    weights,
    expected_returns,
    covariance_matrix,
    lambda_
):
    """
    Función objetivo del método Weighted Sum.
    """

    risk = annual_risk(
        weights,
        covariance_matrix
    )

    ret = annual_return(
        weights,
        expected_returns
    )

    return lambda_ * risk - (1 - lambda_) * ret

def build_constraints():

    return (

        {
            "type": "eq",
            "fun": lambda w: np.sum(w) - 1
        },

    )

def optimize(
    expected_returns,
    covariance_matrix,
    n_lambdas=100,
    risk_free_rate=0.0
):
    """
    Optimiza un portafolio mediante el método Weighted Sum.
    """

    n_assets = len(expected_returns)

    initial_weights = np.ones(n_assets) / n_assets

    bounds = tuple((0, 1) for _ in range(n_assets))

    constraints = build_constraints()

    lambda_values = np.linspace(
        0.0,
        1.0,
        n_lambdas
    )

    portfolio_returns = []
    portfolio_risks = []
    sharpe_ratios = []
    portfolio_weights = []

    for lambda_ in lambda_values:

        result = minimize(
            objective,
            x0=initial_weights,
            args=(
                expected_returns,
                covariance_matrix,
                lambda_
            ),
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