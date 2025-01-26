from mymlpackage.load_data import load_data
from mymlpackage.analyze_missing import analyze_missing
from mymlpackage.create_pairplot import create_pairplot
from mymlpackage.corr_analys import corr_analys
from mymlpackage.class_balance import class_balance
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
