# py_algo

A comprehensive, test-backed collection of Python implementations for foundational data structures and algorithms. The repository also includes Jupyter notebooks that walk through algorithmic analyses and applied problem demos.

## Highlights
- **Core data structures:** Stacks, queues, deques, hash tables, linked lists, and binary trees with traversal helpers.
- **Searching & sorting:** Sequential/binary search variants alongside bubble, merge, and quick sort utilities.
- **Graph toolkit:** Adjacency-list graph with BFS/DFS traversals, vertex metadata, and traversal helpers built on reusable queue utilities.
- **Mathematical helpers:** Recursive and iterative base converters, power and factorial utilities, and summation helpers for lists.
- **String utilities:** Parentheses and palindrome checkers plus infix-to-postfix conversion helpers driven by stack operations.
- **Notebook walkthroughs:** Analysis notebooks—including a hot potato simulation built on the queue implementation—for step-by-step exploration of algorithms.

## Repository structure
- `py_algo/` – Python package with all algorithms and data structures.
  - `data_struct/` – Stack, queue, deque, linked list, and hash table implementations.
  - `math/` – Base conversion, power, factorial, and summation utilities.
  - `search/` – Sequential and binary search helpers.
  - `sort/` – Bubble, merge, and quick sort implementations.
  - `string/` – Palindrome checker, parenthesis validator, and infix converter utilities.
  - `graph/` – Graph representation with breadth-first and depth-first traversals.
  - `tree/` – Binary tree and binary search tree helpers plus traversal utilities.
  - `tests/` – Nose-based unit, system, and integration tests for each module.
- `analysis/` – Jupyter notebooks analyzing algorithms and solving applied problems.
  - `applied_problems/` – Configuration helper and notebook for hot potato simulation using queues.
- `setup.py` – Packaging and test configuration for local installs.

## Installation
1. Ensure Python 3.7+ is available.
2. From the repository root, install the package:
   ```bash
   pip install .
   ```
3. For editable development installs:
   ```bash
   pip install -e .
   ```

## Usage examples
```python
from py_algo.data_struct import Stack
from py_algo.sort import sort_list
from py_algo.search import search

s = Stack()
for value in [1, 2, 3]:
    s.push(value)
last = s.pop()  # 3

sorted_values = sort_list([5, 2, 4, 1], method="merge")
found = search(sorted_values, 4, method="binary")
```

### Graph traversal
```python
from py_algo.graph import Graph
from py_algo.graph.search import bfs, traverse

g = Graph()
for v in "ABCDE":
    g.addVertex(v)
for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]:
    g.addEdge(u, v)

start = g.getVertex("A")
bfs(g, start)
traverse(g.getVertex("E"))
```

## Running tests
Execute the full test suite with nose from the repository root:
```bash
python setup.py test
```

## Notebook exploration
Open the notebooks in `analysis/` with Jupyter Lab or Jupyter Notebook to explore step-by-step analyses. The applied problems folder includes a hot potato simulation that reuses the queue data structure from the package.