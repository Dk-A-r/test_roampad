from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "My first ML package"
LONG_DESCRIPTION = "My first ML package on credit defaults"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="mymlpackage",
    version=VERSION,
    author="Danil Karpov",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license="MIT",
    py_modules=[
        "analyze_missing",
        "class_balance",
        "corr_analys",
        "create_pairplot",
        "eda",
        "load_data",
        "nbgenerate",
    ],
    package_data={"mymlpackage": ["data.csv"]},
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "seaborn",
        "matplotlib",
        "nbconvert",
        "jupyter",
        "nbformat",
    ],  # add any additional packages that
    # needs to be installed
    keywords=["python", "first package"],
    classifiers=["ML"],
)
