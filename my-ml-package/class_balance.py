import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def class_balance(df: pd.DataFrame) -> dict:
    """
    Analyze the balance of default/non-default classes.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        dict: Dictionary containing class balance statistics
    """
    print("5. Анализ баланса классов")
    class_counts = df["Default"].value_counts()
    class_percentages = ((class_counts / len(df)) * 100).round(2)

    plt.figure(figsize=(8, 6))
    class_counts.plot(kind="bar")
    plt.title("Class Distribution")
    plt.xlabel("Default Status")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("./output_pages/png/class_balance.png")
    plt.close()

    def_loans = df.groupby(by="Default")["Loan"].sum()
    def_loans = pd.DataFrame(def_loans)
    def_loans = def_loans.reset_index()
    def_loans.columns = ["Класс займа", "Сумма"]
    sns.barplot(def_loans, x="Класс займа", y="Сумма")
    plt.savefig("./output_pages/png/sum_balance.png")
    plt.close()

    return {
        "counts": class_counts.to_dict(),
        "percentages": class_percentages.to_dict(),
    }
