import os
import nbformat
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# project_root = os.path.abspath(os.path.join(current_dir, '..'))
# sys.path.insert(0, project_root)


my_note = nbformat.v4.new_notebook()
cell0 = nbformat.v4.new_markdown_cell(
    source=["# Предварительный анализ данных в CI/CD"]
)
code = f"""import os
import sys
script_dir = "{current_dir}"
sys.path.append(script_dir)
sys.path.append("{project_root}")
print(script_dir)
print(os.getcwd())
import eda
"""
cell1 = nbformat.v4.new_code_cell(source=code)
cell2 = nbformat.v4.new_markdown_cell(
    source=["# Визуализация пропущенных значений"]
)
cell3 = nbformat.v4.new_markdown_cell(
    source=["![image_miss](output_pages/png/missing_values.png)"]
)

cell4 = nbformat.v4.new_markdown_cell(
    source=["# График попарного распределения"]
)
cell5 = nbformat.v4.new_markdown_cell(
    source=["![image_miss](output_pages/png/pairplot.png)"]
)

cell6 = nbformat.v4.new_markdown_cell(source=["# Матрица корреляций"])
cell7 = nbformat.v4.new_markdown_cell(
    source=["![image_miss](output_pages/png/correlation_matrix.png)"]
)

cell8 = nbformat.v4.new_markdown_cell(
    source=["# График распределения классов"]
)
cell9 = nbformat.v4.new_markdown_cell(
    source=["![image_miss](output_pages/png/class_balance.png)"]
)

cell10 = nbformat.v4.new_markdown_cell(
    source=["# График распределения сумм по классам"]
)
cell11 = nbformat.v4.new_markdown_cell(
    source=["![image_miss](output_pages/png/sum_balance.png)"]
)

my_note.cells = [
    cell0,
    cell1,
    cell2,
    cell3,
    cell4,
    cell5,
    cell6,
    cell7,
    cell8,
    cell9,
    cell10,
    cell11,
]

nbformat.write(my_note, "start_note.ipynb")

subprocess.run(
    [
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--allow-errors",
        "start_note.ipynb",
    ]
)


try:
    text_conclusions = input(
        "Теперь, базируясь на данных предварительного \n"
        "анализа данных, с учетом графиков, сформированных \n"
        "в директории ./output_pages/png, Вы можете сформулировать \n"
        "выводы по изученному датасету. \n"
        "Также диаграммы и выводы Вы можете посмотреть "
        "в сгенерированной части ноутбука "
        "в рабочей директории. "
        "Для отображения всех "
        "выведенных результатов предварительного "
        "анализа данных убедитесь, что настройки отображения "
        "ячеек в части максимума отображаемых строк "
        "позволяют вывести все строки, при необходимости "
        "скорректируйте максимум выводимых строк. "
        "Введите Ваши выводы здесь: "
    )
except EOFError:
    subprocess.run(
        [
            "echo",
            "Среда выполнения не позволяет",
            "использовать интерактивный ввод",
            "либо ввод отсутствует,",
            "поэтому вывод будет типовым.",
            "Внести изменения в вывод на основе",
            "имеющихся данных и диаграмм",
            "можно путем редактирования файла",
            "conclusions.txt в рабочей директории.",
        ]
    )
    with open("conclusions.txt") as f:
        text_conclusions = f.read()

cell12 = nbformat.v4.new_markdown_cell(
    source=["# Выводы на основе предварительного анализа данных"]
)
my_note.cells.append(cell12)

cell13 = nbformat.v4.new_markdown_cell(source=[text_conclusions])
my_note.cells.append(cell13)
nbformat.write(my_note, "start_note.ipynb")

subprocess.run(
    [
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--allow-errors",
        "start_note.ipynb",
    ]
)

subprocess.run(
    [
        "jupyter",
        "nbconvert",
        "--execute",
        "--to",
        "html",
        "--embed-images",
        "start_note.ipynb",
    ]
)
