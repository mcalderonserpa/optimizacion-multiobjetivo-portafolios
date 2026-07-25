import matplotlib.pyplot as plt
from pathlib import Path

def plot_risk_return_assets(
    annual_returns,
    annual_risks,
    save=False,
    filename=None
):
    """
    Grafica el rendimiento anual vs riesgo anual de cada activo.
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        annual_risks,
        annual_returns,
        s=80
    )

    for asset in annual_returns.index:

        ax.annotate(
            asset.upper(),
            (
                annual_risks[asset],
                annual_returns[asset]
            ),
            xytext=(5, 5),
            textcoords="offset points"
        )

    ax.set_title("Annual Return vs Annual Risk")

    ax.set_xlabel("Annual Risk")

    ax.set_ylabel("Annual Return")

    ax.grid(True, alpha=0.3)

    if save:

        if filename is None:

            raise ValueError(
              "Debe especificar un nombre de archivo cuando save=True."
            )
        
        filename = Path(filename)

        filename.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        plt.savefig(
            filename,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()

def plot_pareto_front(
    results,
    title="Portfolio Optimization",
    save=False,
    filename=None
):
    """
    Grafica la frontera de Pareto
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        results["risks"],
        results["returns"],
        c=results["sharpes"],
        cmap="viridis",
        s=8,
        alpha=0.7
    )

    # Máximo Sharpe
    best = results["best_portfolio"]

    ax.scatter(
        best["risk"],
        best["return"],
        color="red",
        marker="*",
        s=300,
        label="Maximum Sharpe Ratio",
        edgecolor="black"
    )

    # Mínimo riesgo
    minimum = results["minimum_risk_portfolio"]

    ax.scatter(
        minimum["risk"],
        minimum["return"],
        color="blue",
        marker="^",
        s=180,
        label="Minimum Risk",
        edgecolor="black"
    )

    ax.set_title(title)

    ax.set_xlabel("Annual Risk")

    ax.set_ylabel("Annual Return")

    ax.grid(True, alpha=0.3)

    ax.legend()

    cbar = fig.colorbar(scatter)

    cbar.set_label("Sharpe Ratio")

    if save:

        if filename is None:
            raise ValueError(
                "Debe proporcionar un nombre de archivo."
            )

        output = Path(filename)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        fig.savefig(
            output,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()