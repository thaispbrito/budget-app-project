# budget-app-project
This is a Python project built for the [freeCodeCamp Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/).
You can view the full project instructions on the certification page.
It allows users to create budget categories, track spending, and visualize spending with a text-based bar chart.

## Features

### Category Class
The `Category` class allows users to:

- Create budget categories
- Add deposits (with optional descriptions)
- Make withdrawals (only if sufficient funds exist)
- Transfer funds between categories
- Check available funds
- View current balance
- Display a formatted ledger with all transactions

### Spending Chart

The `create_spend_chart()` function:

- Accepts a list of categories
- Calculates percentage spent per category (based on withdrawals)
- Generates a **text-based vertical bar chart**
- Labels each category vertically under the chart

---

## Technologies Used

- Python 3
- OOP (Object-Oriented Programming)
- String formatting and alignment
- Generator Expressions
- ASCII art for visual output
- `math.floor` for chart rounding

---

## Tests

Sample test cases are included at the bottom of the main script to demonstrate the behavior of:

- Deposits
- Withdrawals
- Transfers
- Balance calculation
- Spend chart generation

No external libraries or frameworks are required to run the tests.
To view the output, run the script and check the sample_output.txt file for reference.

---

## Project Status
This project is complete and satisfies all requirements of the certification.
However, it may be improved over time for clarity, structure, and additional functionality.

--- 

## How to Run

1. Clone or download the repository.
2. Make sure Python 3 is installed.
3. Run the script:

```bash
python budget_app_project.py

