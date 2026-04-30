# Super User-Friendly CircuitVerse Build Guide

This guide shows how to build the SmartVend Mini circuit slowly and clearly in CircuitVerse.

The circuit has:

- 5 inputs
- 3 outputs
- More than 5 logic gates
- Clear labels
- Test cases that prove it works

## Before You Start

Open CircuitVerse and create a new project.

Suggested project name:

```text
SmartVend Mini - Simple Vending Machine Logic
```

Use the main circuit workspace.

## Part 1: Understand the Signals

### Inputs

Create these five input pins:

| Input label | Meaning |
|---|---|
| C1 | Coin 1 inserted |
| C2 | Coin 2 inserted |
| S | Product selected |
| A | Product available |
| X | Cancel button |

### Outputs

Create these three output pins:

| Output label | Meaning |
|---|---|
| D | Dispense item |
| R | Return money |
| E | Show error |

## Part 2: Place the Input Pins

1. On the left side of the CircuitVerse workspace, place 5 input pins.
2. Put them in a vertical list from top to bottom:

```text
C1
C2
S
A
X
```

3. Label each input clearly.

Your left side should look like this:

```text
C1  Coin 1
C2  Coin 2
S   Product Selected
A   Product Available
X   Cancel
```

Tip: Keep space between pins because many wires will come from them.

## Part 3: Place the Output Pins

1. On the right side of the workspace, place 3 output pins or output LEDs.
2. Put them in a vertical list:

```text
D  Dispense Item
R  Return Money
E  Show Error
```

3. Leave a lot of space between the inputs and outputs. Gates will go in the middle.

## Part 4: Build the Intermediate Signals

The vending machine price is two coins.

So:

```text
P = C1 AND C2
```

`P` means enough payment.

Also:

```text
M = C1 OR C2
```

`M` means at least one coin was inserted.

### Step 4A: Build Enough Payment, P

1. Place one AND gate near the middle-left.
2. Connect `C1` to the first input of the AND gate.
3. Connect `C2` to the second input of the AND gate.
4. Label the output wire:

```text
P = Enough Payment
```

### Step 4B: Build Money Present, M

1. Place one OR gate under the AND gate.
2. Connect `C1` to the first input of the OR gate.
3. Connect `C2` to the second input of the OR gate.
4. Label the output wire:

```text
M = Money Present
```

At this point you have:

```text
C1 AND C2 -> P
C1 OR C2  -> M
```

## Part 5: Add NOT Gates

Some logic needs the opposite of an input.

Add these NOT gates:

| Original signal | NOT output label |
|---|---|
| X | X' |
| A | A' |
| S | S' |
| P | P' |

### Step 5A: Create X'

1. Place a NOT gate.
2. Connect `X` to it.
3. Label the output:

```text
X'
```

### Step 5B: Create A'

1. Place another NOT gate.
2. Connect `A` to it.
3. Label the output:

```text
A'
```

### Step 5C: Create S'

1. Place another NOT gate.
2. Connect `S` to it.
3. Label the output:

```text
S'
```

### Step 5D: Create P'

1. Place another NOT gate.
2. Connect the `P` wire to it.
3. Label the output:

```text
P'
```

## Part 6: Build the Dispense Output D

The dispense rule is:

```text
D = X' . S . A . P
```

This means the item is dispensed only when:

- Cancel is not pressed.
- Product is selected.
- Product is available.
- Enough payment is inserted.

To keep it simple, use three 2-input AND gates.

### Step 6A: First AND gate

Create:

```text
D1 = X' AND S
```

1. Place an AND gate.
2. Connect `X'` to one input.
3. Connect `S` to the other input.
4. Label the output:

```text
D1
```

### Step 6B: Second AND gate

Create:

```text
D2 = A AND P
```

1. Place another AND gate.
2. Connect `A` to one input.
3. Connect `P` to the other input.
4. Label the output:

```text
D2
```

### Step 6C: Final AND gate for D

Create:

```text
D = D1 AND D2
```

1. Place another AND gate.
2. Connect `D1` to one input.
3. Connect `D2` to the other input.
4. Connect the output to the `D` output pin.

Now the dispense output is complete.

## Part 7: Build the Return Money Output R

The return money rule is:

```text
R = M . (X + S . A')
```

This means money is returned when:

- Money exists and cancel is pressed, or
- Money exists and the selected product is unavailable.

### Step 7A: Product unavailable while selected

Create:

```text
R1 = S AND A'
```

1. Place an AND gate.
2. Connect `S` to one input.
3. Connect `A'` to the other input.
4. Label the output:

```text
R1 = Selected but unavailable
```

Important: This same `R1` signal will also be reused later for the error output.

### Step 7B: Cancel OR unavailable

Create:

```text
R2 = X OR R1
```

1. Place an OR gate.
2. Connect `X` to one input.
3. Connect `R1` to the other input.
4. Label the output:

```text
R2
```

### Step 7C: Final AND gate for R

Create:

```text
R = M AND R2
```

1. Place an AND gate.
2. Connect `M` to one input.
3. Connect `R2` to the other input.
4. Connect the output to the `R` output pin.

Now the return money output is complete.

## Part 8: Build the Show Error Output E

The error rule is:

```text
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

This means an error is shown when cancel is not pressed and one of these problems happens:

1. Product is selected and available, but payment is not enough.
2. Product is selected but unavailable.
3. Money was inserted but no product was selected.

We will build three error parts and then combine them.

## Part 8A: Error Part 1 - Not Enough Payment

Create:

```text
E1 = S AND A AND P'
```

Use two AND gates.

### First AND gate

Create:

```text
E1A = S AND A
```

1. Place an AND gate.
2. Connect `S` to one input.
3. Connect `A` to the other input.
4. Label the output:

```text
E1A
```

### Second AND gate

Create:

```text
E1 = E1A AND P'
```

1. Place another AND gate.
2. Connect `E1A` to one input.
3. Connect `P'` to the other input.
4. Label the output:

```text
E1 = Not enough payment
```

## Part 8B: Error Part 2 - Product Unavailable

You already made this signal:

```text
R1 = S AND A'
```

For the error logic, use the same wire and think of it as:

```text
E2 = S AND A'
```

You do not need to build it again.

## Part 8C: Error Part 3 - Money but No Product Selected

Create:

```text
E3 = S' AND M
```

1. Place an AND gate.
2. Connect `S'` to one input.
3. Connect `M` to the other input.
4. Label the output:

```text
E3 = Money but no selection
```

## Part 8D: Combine the Error Parts

Now combine:

```text
E1 OR E2 OR E3
```

Use two OR gates.

### First OR gate

Create:

```text
E12 = E1 OR E2
```

1. Place an OR gate.
2. Connect `E1` to one input.
3. Connect `R1/E2` to the other input.
4. Label the output:

```text
E12
```

### Second OR gate

Create:

```text
EALL = E12 OR E3
```

1. Place another OR gate.
2. Connect `E12` to one input.
3. Connect `E3` to the other input.
4. Label the output:

```text
EALL
```

## Part 8E: Final Error Gate

The error should not show when cancel is pressed.

So create:

```text
E = X' AND EALL
```

1. Place an AND gate.
2. Connect `X'` to one input.
3. Connect `EALL` to the other input.
4. Connect the output to the `E` output pin.

Now the error output is complete.

## Part 9: Final Circuit Checklist

Your circuit should have these signals:

```text
C1, C2, S, A, X
P, M
X', A', S', P'
D1, D2, D
R1, R2, R
E1A, E1, E3, E12, EALL, E
```

Your final outputs are:

```text
D = Dispense Item
R = Return Money
E = Show Error
```

## Part 10: Test the Circuit

Use these tests before taking screenshots.

### Test 1: Correct purchase

Set inputs:

```text
C1 = 1
C2 = 1
S  = 1
A  = 1
X  = 0
```

Expected outputs:

```text
D = 1
R = 0
E = 0
```

Meaning: dispense the item.

### Test 2: Not enough payment

Set inputs:

```text
C1 = 1
C2 = 0
S  = 1
A  = 1
X  = 0
```

Expected outputs:

```text
D = 0
R = 0
E = 1
```

Meaning: show an error because only one coin was inserted.

### Test 3: Product unavailable

Set inputs:

```text
C1 = 1
C2 = 1
S  = 1
A  = 0
X  = 0
```

Expected outputs:

```text
D = 0
R = 1
E = 1
```

Meaning: product is unavailable, so return money and show error.

### Test 4: Cancel after inserting money

Set inputs:

```text
C1 = 1
C2 = 0
S  = 0
A  = 1
X  = 1
```

Expected outputs:

```text
D = 0
R = 1
E = 0
```

Meaning: cancel returns the money.

### Test 5: Idle

Set inputs:

```text
C1 = 0
C2 = 0
S  = 0
A  = 1
X  = 0
```

Expected outputs:

```text
D = 0
R = 0
E = 0
```

Meaning: the machine is waiting.

## Part 11: What Screenshot to Submit

For the best screenshot:

1. Use Test 1.
2. Make sure the labels are visible.
3. Make sure `D` is ON and `R`, `E` are OFF.
4. Save the screenshot as:

```text
screenshots/circuit_design.png
```

Then also take a screenshot of the Python test result:

```text
python src/main.py --test
```

Save it as:

```text
screenshots/python_output.png
```

## Part 12: Easy Presentation Explanation

You can explain the circuit like this:

```text
Our vending machine has five inputs and three outputs.
First, we check if enough payment was inserted using C1 AND C2.
Then we check if any money exists using C1 OR C2.
The dispense output becomes 1 only when payment is enough, the product is selected, the product is available, and cancel is not pressed.
The return output becomes 1 when the user cancels after inserting money or when the product is unavailable.
The error output becomes 1 when payment is not enough, the product is unavailable, or money was inserted without selecting a product.
```

