# Module 2: Basic Python Concepts Assignment

## Overview

This repository contains two Python scripts for the Module 2 assignment of the Tutedude Python course:

1. **math_operations.py**: Performs basic mathematical operations (addition, subtraction, multiplication, division) on two user-provided numbers.
2. **greeting.py**: Creates a personalized greeting by concatenating the user's first and last names.

## Prerequisites

- Python 3.x installed (verify with `python --version`).
- Git installed (verify with `git --version`).
- Visual Studio Code (VS Code) with Git extension enabled.

## Repository Setup

1. **Clone the Repository**:

- Clone this repository to your local machine:

     ```bash
     git clone https://github.com/sakshi892001/Module2_Python_Assignment.git

2. **Navigate to the Repository Folder:**

     ```bash
     cd Module2_Python_Assignment

3. **Run the scripts**:

      ```bash
     python math_operations.py
     python greeting.py

## Task 1: Mathematical Operations

- File: math_operations.py
- Functionality: Prompts the user for two numbers and performs addition, subtraction, multiplication, and division. Handles invalid inputs (e.g., non-numeric values) and division by zero.

## Task 2: Personalized Greeting

- File: greeting.py
- Functionality: Takes the user's first and last names, concatenates them, and prints a personalized greeting. Handles empty inputs.

## Error Handling

- Catches ValueError for non-numeric inputs.
- Checks for division by zero and returns a user-friendly message.

- Validates that first and last names are not empty.
- Catches unexpected errors with a generic message.

## Notes

- Ensure Python is installed and added to your system's PATH.

- Test the scripts with various inputs to verify robustness.
