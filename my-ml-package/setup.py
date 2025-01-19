from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "My first ML package"
LONG_DESCRIPTION = "My first ML package on credit defaults"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="my-ml-package",
    version=VERSION,
    author="Danil Karpov",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed
    keywords=["python", "first package"],
    classifiers=["ML"],
)
