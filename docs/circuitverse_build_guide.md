# CircuitVerse Build Guide

Use this guide to build the SmartVend Mini circuit in CircuitVerse.

## 1. Create Inputs

Create five input pins and label them:

- `C1 - Coin 1`
- `C2 - Coin 2`
- `S - Product Selected`
- `A - Product Available`
- `X - Cancel`

## 2. Create Intermediate Signals

### Enough Payment

Add one AND gate:

```text
P = C1 AND C2
```

Label the output wire `P - Enough Payment`.

### Money Present

Add one OR gate:

```text
M = C1 OR C2
```

Label the output wire `M - Money Present`.

## 3. Build Dispense Output

Equation:

```text
D = X' . S . A . P
```

Steps:

1. Send `X` into a NOT gate to create `X'`.
2. Send `X'`, `S`, `A`, and `P` into a 4-input AND gate.
3. Connect the result to an output pin labeled `D - Dispense Item`.

If your AND gate has only two inputs, combine signals in stages:

```text
T1 = X' AND S
T2 = A AND P
D = T1 AND T2
```

## 4. Build Return Money Output

Equation:

```text
R = M . (X + S . A')
```

Steps:

1. Send `A` into a NOT gate to create `A'`.
2. Use an AND gate for `S . A'`.
3. Use an OR gate for `X + S . A'`.
4. Use an AND gate with `M` and the OR result.
5. Connect to an output pin labeled `R - Return Money`.

## 5. Build Show Error Output

Equation:

```text
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

Steps:

1. You already have `X'` and `A'`.
2. Send `P` into a NOT gate to create `P'`.
3. Send `S` into a NOT gate to create `S'`.
4. Create error term 1: `S . A . P'`.
5. Create error term 2: `S . A'`.
6. Create error term 3: `S' . M`.
7. OR the three error terms together.
8. AND the OR result with `X'`.
9. Connect to an output pin labeled `E - Show Error`.

## 6. Suggested Layout

Place the circuit from left to right:

```text
Inputs -> Intermediate signals -> Output logic -> Output LEDs
```

Recommended label colors:

- Inputs on the left.
- Intermediate labels in the center.
- Output LEDs on the right.

## 7. Important Test Cases

Test these cases in CircuitVerse:

| C1 | C2 | S | A | X | Expected output |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 0 | Dispense=1, Return=0, Error=0 |
| 1 | 0 | 1 | 1 | 0 | Dispense=0, Return=0, Error=1 |
| 1 | 1 | 1 | 0 | 0 | Dispense=0, Return=1, Error=1 |
| 1 | 0 | 0 | 1 | 1 | Dispense=0, Return=1, Error=0 |
| 0 | 0 | 0 | 1 | 0 | Dispense=0, Return=0, Error=0 |

## 8. Optional State Machine

If your group wants to include a sequential component, add two D flip-flops for state bits:

- `Q1`
- `Q0`

Use four states:

| Q1 | Q0 | State |
|---:|---:|---|
| 0 | 0 | Idle |
| 0 | 1 | Money Inserted |
| 1 | 0 | Dispense |
| 1 | 1 | Return/Error |

The combinational output circuit can still control `D`, `R`, and `E`. The state machine is used to show that the system remembers whether money has been inserted between clock pulses.

