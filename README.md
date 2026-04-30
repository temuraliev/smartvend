# Project Title: SmartVend Mini - Simple Vending Machine Logic

## Group Members

| Name | Role |
|---|---|
| Unarov Ahrorbek  | Logic Designer |
| Temur Aliyev  | Python Developer / Presenter |
| Islom Raxmanov  | CircuitVerse Designer |
| Shaxzodbek Turabidinov  | Documentation Lead |
| Soliha Xolova | Testing and AI/LLM Reflection |

## Course

EEE120 Digital Design Fundamentals

## GitHub Repository

https://github.com/temuraliev/smartvend

## Instructor

Dr. Rajan Tirpathi

## Problem Statement

Small vending machines must decide when to release a product, return money, or show an error. This project designs a simple digital vending machine that only dispenses an item when enough payment has been inserted, a product is selected, the product is available, and the cancel button is not pressed.

The same logic is implemented in two ways:

1. A digital logic circuit for CircuitVerse.
2. A Python software prototype that simulates the circuit decisions.

## Inputs

| Input | Symbol | Meaning |
|---|---|---|
| Coin 1 inserted | C1 | First coin/payment signal |
| Coin 2 inserted | C2 | Second coin/payment signal |
| Product selected | S | User selected a product |
| Product available | A | Selected product is in stock |
| Cancel button | X | User wants to cancel |

## Outputs

| Output | Symbol | Meaning |
|---|---|---|
| Dispense item | D | Release the selected product |
| Return money | R | Give inserted money back |
| Show error | E | Show a problem such as not enough payment or no stock |

## Digital Logic Explanation

The product price is treated as two coins. Therefore, enough payment is true only when both coin inputs are true.

Intermediate signals:

```text
P = C1 . C2
M = C1 + C2
```

Where:

- `P` means enough payment.
- `M` means at least one coin was inserted.
- `.` means AND.
- `+` means OR.
- `'` means NOT.

Output equations:

```text
D = X' . S . A . P
R = M . (X + S . A')
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

Explanation:

- The machine dispenses only if payment is enough, a product is selected, it is available, and cancel is not pressed.
- The machine returns money if cancel is pressed after money was inserted, or if the selected product is unavailable.
- The machine shows an error when there is not enough payment, no product selection after money was inserted, or the selected product is unavailable.

## CircuitVerse Link

[SmartVend Mini CircuitVerse Project](https://circuitverse.org/users/425977/projects/smartvend-mini-simple-vending-machine-logic-f68a34e8-7c62-4537-a0f3-0334030dd530)

The verified CircuitVerse design file is included as [SmartVend Mini - Simple Vending Machine Logic.cv](SmartVend%20Mini%20-%20Simple%20Vending%20Machine%20Logic.cv).

## Python Program Explanation

The Python program in [src/main.py](src/main.py) uses the same Boolean equations as the digital circuit. It provides:

- A menu-driven console interface.
- User input for the five circuit inputs.
- Output display for dispense, return money, and error.
- A full truth table option.
- Built-in test cases to verify the most important decisions.

## Presentation

The presentation file is included at [presentation/final_presentation.html](presentation/final_presentation.html).

## How AI/LLM Was Used

AI was used to help organize the idea, draft explanations, generate test cases, and prepare the first version of the Python prototype and presentation text. The group checked the Boolean logic, CircuitVerse behavior, and Python test results to make sure the work was understood and correct.

## How to Run the Python Code

From this project folder:

```bash
python src/main.py
```

To run built-in test cases directly:

```bash
python src/main.py --test
```

To print the full truth table:

```bash
python src/main.py --truth-table
```

## Screenshots

- `circuit_design.png`: screenshot of the CircuitVerse circuit.
- `python_output.png`: screenshot of your Python program output.

## Future Improvements

- Add multiple products with different prices.
- Add memory for inserted money and product inventory.
- Add a counter or state machine for Idle, Money Inserted, Dispense, and Return states.
- Add a seven-segment display for price, stock, or error code.
