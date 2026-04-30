# Slide 1: Title

## SmartVend Mini - Simple Vending Machine Logic

EEE120 Digital Design Fundamentals

Instructor: Dr. Rajan Tirpathi

Team Members:

- Unarov Ahrorbek
- Temur Aliyev
- Islom Raxmanov
- Shaxzodbek Turabidinov
- Soliha Xolova

---

# Slide 2: Problem

Vending machines must make fast and correct decisions:

- Should the item be dispensed?
- Should money be returned?
- Should an error be shown?

Our project solves this using basic digital logic gates.

---

# Slide 3: System Overview

Inputs:

- Coin 1 inserted
- Coin 2 inserted
- Product selected
- Product available
- Cancel button

Outputs:

- Dispense item
- Return money
- Show error

---

# Slide 4: Logic Design

The product price is two coins.

Intermediate logic:

```text
P = C1 . C2
M = C1 + C2
```

Output logic:

```text
D = X' . S . A . P
R = M . (X + S . A')
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

---

# Slide 5: Truth Table or Decision Table

| Situation | Dispense | Return | Error |
|---|---:|---:|---:|
| Enough payment, selected, available | 1 | 0 | 0 |
| Cancel pressed after money | 0 | 1 | 0 |
| Product unavailable | 0 | 1 if money inserted | 1 |
| Not enough payment | 0 | 0 | 1 |
| Money inserted but no selection | 0 | 0 | 1 |
| Idle | 0 | 0 | 0 |

---

# Slide 6: CircuitVerse Design

CircuitVerse project link:

https://circuitverse.org/users/425977/projects/smartvend-mini-simple-vending-machine-logic-f68a34e8-7c62-4537-a0f3-0334030dd530

Circuit screenshot:

```text
screenshots/circuit_design.png
```

Main parts:

- Input switches for C1, C2, S, A, and X
- AND gate for enough payment
- OR gate for money present
- NOT gates for inverted signals
- Output logic for D, R, and E
- Output LEDs for dispense, return, and error

---

# Slide 7: Python Prototype

The Python program uses the same Boolean equations as the circuit.

Features:

- Console menu
- User input
- Truth table display
- Built-in test cases
- Status message explaining each result

Show Python output screenshot here.

---

# Slide 8: Demo

Demo test case:

```text
C1=1, C2=1, S=1, A=1, X=0
```

Expected result:

```text
Dispense item = 1
Return money = 0
Show error = 0
```

Another test:

```text
C1=1, C2=0, S=1, A=1, X=0
```

Expected result:

```text
Dispense item = 0
Return money = 0
Show error = 1
```

---

# Slide 9: AI/LLM Usage

AI was used to help:

- Organize the idea
- Draft Boolean equations
- Generate test cases
- Prepare Python code
- Improve explanation and slide wording

What we checked ourselves:

- The truth table
- CircuitVerse output behavior
- Python test results
- The meaning of each gate and signal

---

# Slide 10: Conclusion

What worked:

- The circuit makes clear vending decisions.
- The Python version matches the circuit logic.
- Test cases confirm expected behavior.

What was difficult:

- Handling all error cases clearly.
- Making the circuit neat and easy to explain.

Future improvement:

- Add multiple products, different prices, inventory memory, and a stronger state machine.
