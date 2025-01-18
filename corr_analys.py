import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def corr_analys(df: pd.DataFrame) -> None:
    """
    Analyze and visualize correlations between numerical features.

    Args:
        df (pd.DataFrame): Input dataset
    """
    print("4. Корреляционный анализ")
    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
    corr_matrix = df[numerical_cols].corr().round(2)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0, fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig("./output_pages/png/correlation_matrix.png")
    plt.close()
