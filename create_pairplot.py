import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def create_pairplot(df: pd.DataFrame) -> None:
    """
    Create pairwise distribution plots for numerical features.

    Args:
        df (pd.DataFrame): Input dataset
    """
    print("3. Создание парных графиков распределения для числовых признаков")

    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
    numerical_cols = numerical_cols[numerical_cols != "Default"].tolist()
    Path("./output_pages/png/").mkdir(parents=True, exist_ok=True)

    sns.pairplot(df, vars=numerical_cols, hue="Default", diag_kind="hist")
    plt.savefig("./output_pages/png/pairplot.png")
    plt.close()
