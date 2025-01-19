import pandas as pd


def load_data(file_path: str = "data.csv") -> pd.DataFrame:
    print("1. Предварительный обзор данных")
    df = pd.read_csv(file_path)

    numeric_cols = df.select_dtypes(include=["float64"]).columns
    df[numeric_cols] = df[numeric_cols].round(2)
    print("Data is loaded")
    print("\nDataset Overview:")
    print("-" * 50)
    print("\nFirst few rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nColumn names:", list(df.columns))
    print("\nData types:\n", df.dtypes, sep="")
    return df
