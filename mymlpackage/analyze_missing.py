import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def analyze_missing(df: pd.DataFrame) -> dict:
    """
    Analyze missing values in the dataset.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        dict: Dictionary containing missing values analysis
    """

    print("2. Анализ пропущенных значений")
    missing_values = df.isnull().sum()
    missing_percentages = (missing_values / len(df)) * 100
    print(missing_percentages)
    # create directory for graphs if absent
    Path("./output_pages/png/").mkdir(parents=True, exist_ok=True)

    # if missing_values.sum() > 0:
    plt.figure(figsize=(10, 6))
    plt.title("Missing Values by Column")
    plt.ylabel("Percentage of Missing Values")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("./output_pages/png/missing_values.png")
    plt.close()

    if missing_values.sum() == 0:
        print(
            "As missing values are all at zero, the visualisation"
            + " will not have much sense"
        )

    return {
        "missing_counts": missing_values.to_dict(),
        "missing_percentages": missing_percentages.to_dict(),
    }
