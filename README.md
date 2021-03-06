# py_algo (IN PROGRESS)

## Package Description
This repository has python implementation of all the fundamental data structures and algorithms. One of the next courses I am going to create will be on "Algorithms and Data Structures", and this repo is a sample. It contains python implementation of fundamentals data structures, search, sort, math, and graph algorithms. The package is self-contained; and unit tested & system tested using nose.

## Folder Description
- `py_algo` - contains python package which contains python implementation of all the fundamental data structures and algorithms.
- `analysis` - contains algorithmic analysis of the algorithms in py_algo in jupyter notebooks.

## Installation Procedure
Download the package. Open the terminal, and change current directory to the directory containing the setup.py file. Install the package using the following command:

`pip install .`

## Test
Each function/method in the package is unit tested and each module in the package is system and integration tested or using well chosen test case. Tests can be executed using the test suite `nose`. The test cases can be found in the following directory "./py_algo/tests". To run the test change current directory to the directory containing the setup.py file and type the following command:

`python setup.py test`
