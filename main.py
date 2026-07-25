from src.data_loader import load_prices
from src.metrics import (
    calculate_returns,
    expected_returns,
    covariance_matrix
)

from src.methods.monte_carlo import optimize as monte_carlo
from src.methods.epsilon_constraint import optimize as epsilon_constraint
from src.methods.weighted_sum import optimize as weighted_sum

from src.visualization import plot_pareto_front

METHODS = {
    "monte_carlo": {
        "title": "Monte Carlo Portfolio Optimization",
        "function": monte_carlo,
        "params": {
            "n_portfolios": 50000
        }
    },

    "epsilon_constraint": {
        "title": "ε-Constraint Portfolio Optimization",
        "function": epsilon_constraint,
        "params": {
            "n_points": 100
        }
    },

    "weighted_sum": {
        "title": "Weighted Sum Portfolio Optimization",
        "function": weighted_sum,
        "params": {
            "n_lambdas": 100
        }
    }
}

METHOD = "weighted_sum"

def main():

    symbols = [
        "amd",
        "amzn", 
        "nvda",  
        "pypl", 
        "intc", 
        "adbe", 
        "msft"
    ]

    prices = load_prices(symbols, "data/raw")

    returns = calculate_returns(prices)

    mu = expected_returns(returns)

    cov = covariance_matrix(returns)

    method = METHODS[METHOD]

    optimize = method["function"]

    results = optimize(
        expected_returns=mu,
        covariance_matrix=cov,
        risk_free_rate=0.0,
        **method["params"]
    )

    plot_pareto_front(
        results,
        title=method["title"]
    )

    print("\nBest Portfolio\n")

    best = results["best_portfolio"]

    print(f"Annual Return : {best['return']:.2%}")
    print(f"Annual Risk   : {best['risk']:.2%}")
    print(f"Sharpe Ratio  : {best['sharpe']:.4f}")

    print("\nWeights")

    for asset, weight in zip(symbols, best["weights"]):
        print(f"{asset:<8} {weight:.2%}")


if __name__ == "__main__":
    main()