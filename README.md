# Optimización Multiobjetivo de Portafolios Financieros

Proyecto académico desarrollado como parte del pregrado en Matemáticas de la Universidad Industrial de Santander.

El proyecto estudia la teoría de la **Optimalidad de Pareto** y su aplicación a la optimización de portafolios financieros mediante el modelo de **Markowitz**.

Para ello se implementaron diferentes algoritmos de optimización multiobjetivo en Python y se comparó su desempeño utilizando datos históricos reales del mercado bursátil.

---

## Objetivos

- Estudiar los fundamentos de la Optimalidad de Pareto.
- Implementar diferentes métodos de optimización multiobjetivo.
- Aplicar dichos métodos al problema de selección de portafolios de Markowitz.
- Comparar el desempeño de cada método mediante el índice de Sharpe.

---

## Métodos implementados

- Monte Carlo
- ε-Constraint
- Weighted Sum

Cada método genera una aproximación de la Frontera de Pareto y permite identificar tanto el portafolio de máxima razón de Sharpe como el portafolio de mínima varianza.

---

## Tecnologías utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy

---

## Estructura del proyecto

```text
portfolio-optimization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── multiobjetivoStockMarket.ipynb
│
├── results/
│
├── src/
│   ├── methods/
│   │   ├── monte_carlo.py
│   │   ├── epsilon_constraint.py
│   │   └── weighted_sum.py
│   │
│   ├── data_loader.py
│   ├── metrics.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Ejecución

Seleccione el método de optimización en `main.py`:

```python
METHOD = "monte_carlo"
```

Los métodos disponibles son:

```python
"monte_carlo"
"epsilon_constraint"
"weighted_sum"
```

Finalmente ejecute:

```bash
python main.py
```

El programa descargará automáticamente los datos históricos desde Yahoo Finance, realizará la optimización y mostrará la Frontera de Pareto junto con la información del portafolio óptimo.

---

## Resultados

El proyecto permite:

- Construir la Frontera de Pareto.
- Obtener el portafolio de máxima coeficiente de Sharpe.
- Obtener el portafolio de mínima varianza.
- Visualizar la relación riesgo-retorno para cada estrategia.

Las figuras generadas pueden almacenarse en la carpeta `results/`.

---

## Documento

El informe completo puede consultarse en:

```
docs/Proyecto_Optimalidad_de_Pareto.pdf
```

---

## Autores

- Miguel Ricardo Calderón Serpa
- Karen Julieth Bermúdez Calderón
- Nazhly Zharith Flórez Martínez

**Universidad Industrial de Santander**