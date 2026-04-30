# SmartVend Mini Logic Design

## Main Idea

The vending machine should dispense an item only when all correct conditions are true:

1. Enough money is inserted.
2. A product is selected.
3. The selected product is available.
4. The cancel button is not pressed.

If the user cancels or the product is unavailable after money is inserted, the machine returns money. If something is wrong, it shows an error.

## Inputs

| Symbol | Input | Description |
|---|---|---|
| C1 | Coin 1 inserted | First coin signal |
| C2 | Coin 2 inserted | Second coin signal |
| S | Product selected | Product selection signal |
| A | Product available | Stock availability signal |
| X | Cancel button | Cancel signal |

## Outputs

| Symbol | Output | Description |
|---|---|---|
| D | Dispense item | Releases product |
| R | Return money | Returns inserted money |
| E | Show error | Shows invalid condition |

## Intermediate Signals

```text
P = C1 . C2
M = C1 + C2
```

`P` means enough payment. The machine price is two coins, so both coin inputs must be 1.

`M` means money is present. It is true when at least one coin was inserted.

## Boolean Equations

```text
D = X' . S . A . P
R = M . (X + S . A')
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

## Gate Count

The CircuitVerse circuit uses more than five logic gates:

1. AND gate for enough payment, `P = C1 . C2`.
2. OR gate for money present, `M = C1 + C2`.
3. NOT gate for cancel, `X'`.
4. NOT gate for product available, `A'`.
5. NOT gate for product selected, `S'`.
6. NOT gate for enough payment, `P'`.
7. AND gates for dispense, return, and error terms.
8. OR gates to combine return and error conditions.

## Decision Table

| Situation | Required input condition | Dispense D | Return R | Error E |
|---|---|---:|---:|---:|
| Idle | No money and no selected product | 0 | 0 | 0 |
| Correct purchase | C1=1, C2=1, S=1, A=1, X=0 | 1 | 0 | 0 |
| Cancel with money | M=1, X=1 | 0 | 1 | 0 |
| Product unavailable | S=1, A=0, X=0 | 0 | 1 if M=1 | 1 |
| Not enough payment | S=1, A=1, P=0, X=0 | 0 | 0 | 1 |
| Money but no selection | M=1, S=0, X=0 | 0 | 0 | 1 |

## Optional Sequential Extension

A simple state machine can be added using two D flip-flops.

| State bits | State name | Meaning |
|---|---|---|
| 00 | Idle | Waiting for coins |
| 01 | Money Inserted | At least one coin was inserted |
| 10 | Dispense | Product is released for one clock cycle |
| 11 | Return/Error | Money is returned or error is displayed for one clock cycle |

Simple transition plan:

| Current state | Condition | Next state |
|---|---|---|
| Idle | M=0 | Idle |
| Idle | M=1 and X=0 | Money Inserted |
| Money Inserted | X=1 | Return/Error |
| Money Inserted | S=1, A=0 | Return/Error |
| Money Inserted | P=1, S=1, A=1, X=0 | Dispense |
| Money Inserted | Otherwise | Money Inserted |
| Dispense | Next clock | Idle |
| Return/Error | Next clock | Idle |

For an easier CircuitVerse build, the combinational design can be submitted as the main working circuit, and the sequential part can be shown as an optional extension or state diagram.

