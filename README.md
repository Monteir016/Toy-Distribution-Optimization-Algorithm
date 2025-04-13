# Toy Distribution Optimization Algorithm

## Overview

This project solves a toy distribution optimization problem using linear programming. The goal is to maximize the number of toys distributed to children while respecting constraints related to factory stock, export limits, and minimum toy requirements for each country.

The problem is modeled and solved using the `PuLP` library, which provides tools for linear programming and optimization.

## Features

- **Input Parsing**: Reads input data for factories, countries, and children requests.
- **Linear Programming Model**: Uses `PuLP` to define and solve the optimization problem.
- **Constraints**:
  - Each child can receive at most one toy.
  - Factories cannot exceed their stock limits.
  - Export limits and minimum toy requirements for countries are respected.
- **GLPK Solver**: Uses the GLPK solver to find the optimal solution.

## Input Format

The program expects input in the following format:

1. Three integers:
   - `n`: Number of factories.
   - `m`: Number of countries.
   - `t`: Number of children requests.
2. `n` lines, each containing:
   - `factoryId`: ID of the factory.
   - `idCountry`: ID of the country where the factory is located.
   - `factory_stock`: Number of toys available in the factory.
3. `m` lines, each containing:
   - `CountryId`: ID of the country.
   - `exportLimit`: Maximum number of toys that can be exported from the country.
   - `minToys`: Minimum number of toys that must be distributed to children in the country.
4. `t` lines, each containing:
   - `idChild`: ID of the child.
   - `country_id`: ID of the country where the child is located.
   - A list of `factoryId`s from which the child can receive toys.

### Example Input
`3 2 4 1 1 10 2 1 5 3 2 8 1 10 5 2 15 3 1 1 1 2 2 1 1 3 3 2 2 3 4 2 3`

## Output Format

The program outputs:

- The maximum number of toys that can be distributed to children while respecting all constraints.
- `-1` if the problem is infeasible (i.e., no valid solution exists).

### Example Output
`4`

## How It Works

1. **Input Parsing**: The `readInput()` function reads and processes the input data.
2. **Linear Programming Model**:
   - Variables: Represents valid child-factory pairs.
   - Objective Function: Maximizes the number of toys distributed.
   - Constraints:
     - Each child receives at most one toy.
     - Factories cannot exceed their stock limits.
     - Export limits and minimum toy requirements for countries are respected.
3. **GLPK Solver**: The problem is solved using the GLPK solver provided by `PuLP`.
4. **Output**: The program prints the maximum number of toys distributed or `-1` if no solution exists.

## How to Run

### Prerequisites

- Python 3.x
- `PuLP` library installed. Install it using:
`pip install pulp`

### Running the Program
1. Save the input data in a file (e.g., `input.txt`).
2. Run the program and provide the input file
`python proj.py < input.txt`

### Example Usage
Input file (input.txt):
````
3 2 4
1 1 10
2 1 5
3 2 8
1 10 5
2 15 3
1 1 1 2
2 1 1 3
3 2 2 3
4 2 3
````

Run the program:
`python [proj.py] < input.txt`
Output:
`4`

## Dependencies
- **Python** 3.x
- **PuLP**: A Python library for linear programming.

Key Functions
`readInput()`
Parses the input data and returns the number of factories, countries, children requests, and their respective details.

`solveProblem(n, m, t, factories, countries, children_requests)`
Defines and solves the linear programming problem using PuLP.

`main()`
Main function that orchestrates input reading and problem solving.

## Author
Developed by Guilherme Monteiro. For more information, visit [my GitHub profile](https://github.com/Monteir016).
