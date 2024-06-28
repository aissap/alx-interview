# Island Perimeter

This project contains a function to calculate the perimeter of an island described in a grid.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7)
- No module imports are allowed
- All modules and functions must be documented
- All files must be executable

## Task 0: Island Perimeter

For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

### Concepts Needed:

- **2D Arrays (Matrices):**

  - Accessing and iterating over elements in a 2D array.
  - Understanding how to navigate through adjacent cells (horizontally and vertically).

- **Conditional Logic:**

  - Applying conditions to determine whether a cell contributes to the perimeter of the island.

- **Counting Techniques:**

  - Developing a method to count the edges that contribute to the island’s perimeter.

- **Problem-Solving Strategies:**

  - Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

- **Python Programming:**
  - Nested loops for iterating over grid cells.
  - Conditional statements to check the status of adjacent cells.

### Resources:

- **Python Official Documentation:**
  - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists within lists in Python.
- **GeeksforGeeks Articles:**

  - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.

- **TutorialsPoint:**

  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

- **YouTube Tutorials:**
  - [Python 2D arrays and lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

### Function

#### island_perimeter

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the map with 0s as water and 1s as land.

    Returns:
        int: The perimeter of the island.
    """
```
