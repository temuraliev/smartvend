from dataclasses import dataclass
from itertools import product
import sys


@dataclass(frozen=True)
class MachineInputs:
    coin1: bool
    coin2: bool
    product_selected: bool
    product_available: bool
    cancel: bool


@dataclass(frozen=True)
class MachineOutputs:
    enough_payment: bool
    money_present: bool
    dispense_item: bool
    return_money: bool
    show_error: bool
    message: str


def evaluate_logic(inputs: MachineInputs) -> MachineOutputs:
    """Evaluate the same Boolean logic used in the digital circuit."""
    c1 = inputs.coin1
    c2 = inputs.coin2
    s = inputs.product_selected
    a = inputs.product_available
    x = inputs.cancel

    enough_payment = c1 and c2
    money_present = c1 or c2

    dispense_item = (not x) and s and a and enough_payment
    return_money = money_present and (x or (s and not a))
    show_error = (not x) and (
        (s and a and not enough_payment)
        or (s and not a)
        or ((not s) and money_present)
    )

    message = describe_result(inputs, dispense_item, return_money, show_error)

    return MachineOutputs(
        enough_payment=enough_payment,
        money_present=money_present,
        dispense_item=dispense_item,
        return_money=return_money,
        show_error=show_error,
        message=message,
    )


def describe_result(
    inputs: MachineInputs,
    dispense_item: bool,
    return_money: bool,
    show_error: bool,
) -> str:
    if dispense_item:
        return "Dispense item: enough payment, product selected, and product available."
    if inputs.cancel and return_money:
        return "Return money: cancel button was pressed."
    if inputs.product_selected and not inputs.product_available:
        if return_money:
            return "Return money and show error: selected product is unavailable."
        return "Show error: selected product is unavailable."
    if inputs.product_selected and inputs.product_available and not (inputs.coin1 and inputs.coin2):
        return "Show error: payment is not enough."
    if (inputs.coin1 or inputs.coin2) and not inputs.product_selected:
        return "Show error: money inserted but no product selected."
    if inputs.cancel:
        return "Cancel pressed, but no money was inserted."
    return "Idle: waiting for coins and product selection."


def ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in {"y", "yes", "1"}:
            return True
        if answer in {"n", "no", "0"}:
            return False
        print("Please enter y or n.")


def read_inputs_from_user() -> MachineInputs:
    print("\nEnter the five vending machine inputs.")
    return MachineInputs(
        coin1=ask_yes_no("Coin 1 inserted"),
        coin2=ask_yes_no("Coin 2 inserted"),
        product_selected=ask_yes_no("Product selected"),
        product_available=ask_yes_no("Product available"),
        cancel=ask_yes_no("Cancel button pressed"),
    )


def display_outputs(inputs: MachineInputs, outputs: MachineOutputs) -> None:
    print("\nInputs")
    print(f"  Coin 1 inserted     : {int(inputs.coin1)}")
    print(f"  Coin 2 inserted     : {int(inputs.coin2)}")
    print(f"  Product selected    : {int(inputs.product_selected)}")
    print(f"  Product available   : {int(inputs.product_available)}")
    print(f"  Cancel button       : {int(inputs.cancel)}")

    print("\nIntermediate signals")
    print(f"  Enough payment (P)  : {int(outputs.enough_payment)}")
    print(f"  Money present (M)   : {int(outputs.money_present)}")

    print("\nOutputs")
    print(f"  Dispense item (D)   : {int(outputs.dispense_item)}")
    print(f"  Return money (R)    : {int(outputs.return_money)}")
    print(f"  Show error (E)      : {int(outputs.show_error)}")
    print(f"\nStatus: {outputs.message}\n")


def print_truth_table() -> None:
    headers = [
        "C1",
        "C2",
        "S",
        "A",
        "X",
        "P",
        "M",
        "D",
        "R",
        "E",
    ]
    print(" ".join(f"{header:>2}" for header in headers))
    print("-" * 31)
    for c1, c2, s, a, x in product([False, True], repeat=5):
        inputs = MachineInputs(c1, c2, s, a, x)
        outputs = evaluate_logic(inputs)
        values = [
            c1,
            c2,
            s,
            a,
            x,
            outputs.enough_payment,
            outputs.money_present,
            outputs.dispense_item,
            outputs.return_money,
            outputs.show_error,
        ]
        print(" ".join(f"{int(value):>2}" for value in values))


def run_tests() -> bool:
    test_cases = [
        (
            "dispense when payment is enough and product is available",
            MachineInputs(True, True, True, True, False),
            (True, False, False),
        ),
        (
            "return money when cancel is pressed after inserting money",
            MachineInputs(True, False, False, True, True),
            (False, True, False),
        ),
        (
            "show error when payment is not enough",
            MachineInputs(True, False, True, True, False),
            (False, False, True),
        ),
        (
            "return money and show error when product is unavailable",
            MachineInputs(True, True, True, False, False),
            (False, True, True),
        ),
        (
            "show error when money is inserted but no product is selected",
            MachineInputs(False, True, False, True, False),
            (False, False, True),
        ),
        (
            "stay idle when no input is active",
            MachineInputs(False, False, False, True, False),
            (False, False, False),
        ),
    ]

    passed = 0
    for name, inputs, expected in test_cases:
        outputs = evaluate_logic(inputs)
        actual = (
            outputs.dispense_item,
            outputs.return_money,
            outputs.show_error,
        )
        if actual == expected:
            passed += 1
            print(f"PASS: {name}")
        else:
            print(f"FAIL: {name}")
            print(f"  Expected D,R,E = {tuple(int(v) for v in expected)}")
            print(f"  Actual   D,R,E = {tuple(int(v) for v in actual)}")

    print(f"\n{passed}/{len(test_cases)} tests passed.")
    return passed == len(test_cases)


def run_menu() -> None:
    while True:
        print("SmartVend Mini - Vending Machine Logic")
        print("1. Evaluate one input case")
        print("2. Show full truth table")
        print("3. Run built-in tests")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            inputs = read_inputs_from_user()
            outputs = evaluate_logic(inputs)
            display_outputs(inputs, outputs)
        elif choice == "2":
            print()
            print_truth_table()
            print()
        elif choice == "3":
            print()
            run_tests()
            print()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3, or 4.\n")


def main() -> int:
    if "--test" in sys.argv:
        return 0 if run_tests() else 1
    if "--truth-table" in sys.argv:
        print_truth_table()
        return 0
    run_menu()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

