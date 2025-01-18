import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_data import load_data
from analyze_missing import analyze_missing
from create_pairplot import create_pairplot
from corr_analys import corr_analys
from class_balance import class_balance
import nbformat

my_note = nbformat.v4.new_notebook()
df = load_data()
am = analyze_missing(df)
print(am)
print(
    "Таблица распределения пропущенных значений"
    + " сохранена в \n"
    + "./output_pages/png/missing_values.png"
)
pp = create_pairplot(df)
print(
    "График попарного распределения сохранен в \n"
    + "./output_pages/png/pairplot.png"
)
corr_analys(df)
print(
    "Матрица корреляций сохранена в \n"
    + "./output_pages/png/correlation_matrix.png"
)
cb = class_balance(df)
print(cb)
print(
    "График распределения классов сохранен в \n"
    + "./output_pages/png/class_balance.png"
)
print(
    "График распределения сумм по классам сохранен в \n"
    + "./output_pages/png/sum_balance.png"
)
# text_conclusions = input(
#    "Теперь, базируясь на данных предварительного \n"
#    "анализа данных, с учетом графиков, сформированных \n"
#    "в директории ./output_pages/png, Вы можете сформулировать \n"
#    "выводы по изученному датасету. \n"
#    "Введите Ваши выводы здесь: "
# )

# with open("text_conclusions.txt", "w") as f:
#    f.write(text_conclusions)
