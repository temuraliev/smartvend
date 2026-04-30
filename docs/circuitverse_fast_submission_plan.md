# Fast CircuitVerse Submission Plan

## Can This Be Built Automatically With the CircuitVerse API?

Not fully. CircuitVerse has an official API for authentication, user/project information, groups, assignments, grades, collaborators, and project metadata actions such as update/fork. However, the actual simulator save flow for circuit data is handled by the website simulator session.

For this project, the safest approach is:

1. Build the circuit in the CircuitVerse simulator.
2. Save it online from your own CircuitVerse account.
3. Copy the final project link into `circuitverse_link.txt`, `README.md`, and the presentation.

## Fastest Build Method

Use the manual gate design from `docs/circuitverse_build_guide.md`. It is easier to explain during presentation than an auto-generated circuit.

### Inputs

Create five input pins:

```text
C1, C2, S, A, X
```

### Outputs

Create three output pins:

```text
D, R, E
```

### Intermediate Signals

```text
P = C1 . C2
M = C1 + C2
```

### Final Output Equations

```text
D = X' . S . A . P
R = M . (X + S . A')
E = X' . [(S . A . P') + (S . A') + (S' . M)]
```

## Optional CircuitVerse Combinational Analysis Method

CircuitVerse also has a Combinational Analysis tool that can generate a circuit from input/output truth-table values.

Use:

```text
Inputs: C1, C2, S, A, X
Outputs: D, R, E
```

Then fill the truth table values from:

```text
docs/truth_table.csv
```

This method can be faster, but the generated circuit may be harder to explain than the manual gate design.

## What to Screenshot

After building the circuit:

1. Set `C1=1, C2=1, S=1, A=1, X=0`.
2. Confirm `D=1, R=0, E=0`.
3. Take a screenshot and save it as:

```text
screenshots/circuit_design.png
```

Then test:

```text
C1=1, C2=0, S=1, A=1, X=0
```

Expected:

```text
D=0, R=0, E=1
```

## Final Link Updates

Paste the CircuitVerse link in:

- `circuitverse_link.txt`
- `README.md`
- `submission_summary.md`
- Slide 6 in `presentation/final_presentation.md` or `presentation/final_presentation.html`

