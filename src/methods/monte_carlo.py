import numpy as np

from src.metrics import (
    annual_return,
    annual_risk,
    sharpe_ratio
)

def generate_weights(n_assets):
    """
    Genera un portafolio aleatorio cuyos pesos suman 1.
    """

    weights = np.random.random(n_assets)

    weights /= weights.sum()

    return weights

def evaluate_portfolio(
    weights,
    expected_returns,
    covariance_matrix,
    risk_free_rate=0.0
):
    """
    Evalúa un portafolio.

    Parameters
    ----------
    weights : np.ndarray
        Pesos del portafolio.

    expected_returns : pd.Series
        Retornos esperados anualizados.

    covariance_matrix : pd.DataFrame
        Matriz anualizada de covarianzas.

    risk_free_rate : float
        Tasa libre de riesgo.

    Returns
    -------
    tuple
        (retorno, riesgo, sharpe)
    """

    portfolio_ret = annual_return(
        weights,
        expected_returns
    )

    portfolio_risk = annual_risk(
        weights,
        covariance_matrix
    )

    portfolio_sharpe = sharpe_ratio(
        portfolio_ret,
        portfolio_risk,
        risk_free_rate
    )

    return (
        portfolio_ret,
        portfolio_risk,
        portfolio_sharpe
    )

def optimize(
    expected_returns,
    covariance_matrix,
    n_portfolios=10000,
    risk_free_rate=0.0
):
    """
    Optimización Monte Carlo.
    """

    n_assets = len(expected_returns)

    portfolio_returns = np.zeros(n_portfolios)

    portfolio_risks = np.zeros(n_portfolios)

    sharpe_ratios = np.zeros(n_portfolios)

    portfolio_weights = np.zeros(
        (n_portfolios, n_assets)
    )

    for i in range(n_portfolios):

        weights = generate_weights(n_assets)

        ret, risk, sharpe = evaluate_portfolio(
            weights,
            expected_returns,
            covariance_matrix,
            risk_free_rate
        )

        portfolio_returns[i] = ret

        portfolio_risks[i] = risk

        sharpe_ratios[i] = sharpe

        portfolio_weights[i] = weights

    best_index = np.argmax(sharpe_ratios)

    min_risk_index = np.argmin(portfolio_risks)

    best_portfolio = {
    "weights": portfolio_weights[best_index],
    "return": portfolio_returns[best_index],
    "risk": portfolio_risks[best_index],
    "sharpe": sharpe_ratios[best_index]
}
    
    minimum_risk_portfolio = {
    "weights": portfolio_weights[min_risk_index],
    "return": portfolio_returns[min_risk_index],
    "risk": portfolio_risks[min_risk_index],
    "sharpe": sharpe_ratios[min_risk_index]
}

    return {
    "returns": portfolio_returns,
    "risks": portfolio_risks,
    "sharpes": sharpe_ratios,
    "weights": portfolio_weights,
    "best_portfolio": best_portfolio,
    "minimum_risk_portfolio": minimum_risk_portfolio
}