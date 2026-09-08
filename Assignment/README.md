# Assignment 1 - Personal Finance Calculator

A simple command-line Personal Finance Calculator written in Python.

## Description

This program helps users track their income and expenses, then generates a summary report showing total income, total expenses, savings, and whether their spending is affordable.

## Features

- Accepts multiple income entries (up to 10)
- Accepts multiple expense entries (up to 10)
- Validates that all entered amounts are valid numbers
- Calculates:
  - Total Income
  - Total Expenses
  - Savings (Income - Expenses)
  - Percentage of income saved
  - Affordability status (Yes/No)

## How to Run

```bash
python Assn_1.py
```

## Usage Example

```
=== Personal Finance Calculator ===
Enter your name: John

--- INCOME ---
Enter income amount: 5000
Do you want to add another income? (y/n): n

--- EXPENSES ---
Enter expense amount: 3000
Do you want to add another expense? (y/n): n

------------------------------
PERSONAL FINANCE REPORT
Name: John
------------------------------
Total Income: 5000.0
Total Expenses: 3000.0
Savings: 2000.0
Percent Saved: 40.0
Affordable: Yes
```

## Functions

| Function | Description |
|----------|-------------|
| `get_amount(text)` | Prompts the user for a numeric amount and validates the input in a loop until a valid number is entered. |
| `main()` | Main program flow — collects name, income entries, expense entries, and prints the finance report. |

## Requirements

- Python 3.x
- No external libraries required
