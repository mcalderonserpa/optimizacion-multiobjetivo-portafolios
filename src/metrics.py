import pandas as pd
import numpy as np


def calculate_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los retornos diarios de cada activo.
    """
    return prices.pct_change().dropna()

def expected_returns(
    returns: pd.DataFrame,
    trading_days: int = 252
):
    """
    Calcula el retorno anual esperado.
    """
    return returns.mean() * trading_days

def covariance_matrix(
    returns: pd.DataFrame,
    trading_days: int = 252
):
    """
    Calcula la matriz anualizada de covarianzas.
    """
    return returns.cov() * trading_days

def annual_return(weights, expected_returns):
    """
    Calcula el retorno esperado de un portafolio.
    """
    return np.dot(weights, expected_returns)

def annual_risk(weights, covariance):
    """
    Calcula la volatilidad (riesgo) de un portafolio.
    """
    return np.sqrt(
        weights.T @ covariance @ weights
    )

def sharpe_ratio(
    portfolio_return,
    portfolio_risk,
    risk_free_rate=0.0
):
    """
    Calcula el índice de Sharpe.
    """

    return (
        portfolio_return - risk_free_rate
    ) / portfolio_risk

def asset_risk(
    returns,
    trading_days=252
):
    """
    Calcula el riesgo anual de cada activo.
    """

    return returns.std() * np.sqrt(trading_days)