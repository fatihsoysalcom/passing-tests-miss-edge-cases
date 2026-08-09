def calculate_final_price(base_price: float, discount_rate: float) -> float:
    """
    Calculates the final price after applying a discount.
    Discount rate is expected as a percentage (e.g., 10 for 10%).
    """
    if not isinstance(base_price, (int, float)) or not isinstance(discount_rate, (int, float)):
        raise TypeError("Base price and discount rate must be numeric.")

    # The core logic, which might be too simplistic for real-world scenarios
    discount_amount = base_price * (discount_rate / 100)
    final_price = base_price - discount_amount

    # The function as written does not explicitly handle edge cases like
    # negative discount rates, discount rates > 100%, or negative base prices.
    # A passing test suite might not expose these implicit behaviors.
    return final_price

def run_tests():
    print("--- Running Initial Test Suite ---")

    # These tests pass, giving a false sense of security about the function's robustness.
    # They only cover the 'happy path' and expected ranges.

    # Test Case 1: Standard discount
    price1 = calculate_final_price(100, 10)
    assert price1 == 90.0, f"Test 1 Failed: Expected 90.0, got {price1}"
    print(f"Test 1 Passed: 100 with 10% discount -> {price1}")

    # Test Case 2: Zero discount
    price2 = calculate_final_price(200, 0)
    assert price2 == 200.0, f"Test 2 Failed: Expected 200.0, got {price2}"
    print(f"Test 2 Passed: 200 with 0% discount -> {price2}")

    # Test Case 3: Full discount
    price3 = calculate_final_price(50, 100)
    assert price3 == 0.0, f"Test 3 Failed: Expected 0.0, got {price3}"
    print(f"Test 3 Passed: 50 with 100% discount -> {price3}")

    print("\nInitial Test Suite PASSED! (But is it truly robust?)\n")

    print("--- Exploring Uncovered Scenarios ---")
    print("These scenarios highlight what the 'passing' tests *didn't* check.")

    # Scenario 1: Negative discount rate (e.g., a surcharge or an error?)
    # The initial tests don't cover this business rule. The function implicitly treats it as a surcharge.
    price4 = calculate_final_price(100, -10)
    print(f"Scenario 1: 100 with -10% discount -> {price4}")
    if price4 == 110.0:
        print("  Observation: Function implicitly applies a surcharge for negative discount.")
        print("  Question: Is this the intended business rule? The tests didn't specify.")
    else:
        print("  Unexpected behavior for negative discount rate.")

    # Scenario 2: Discount rate > 100% (should result in 0 or an error, not negative price)
    # This is a critical bug missed by the initial tests.
    price5 = calculate_final_price(100, 150)
    print(f"Scenario 2: 100 with 150% discount -> {price5}")
    if price5 < 0:
        print("  CRITICAL BUG: Discount rate > 100% results in negative final price!")
        print("  This indicates a lack of boundary testing in the initial suite.")
    else:
        print("  Unexpected behavior for discount rate > 100%.")

    # Scenario 3: Negative base price (how should it be handled?)
    # Another edge case not covered by the passing tests.
    price6 = calculate_final_price(-50, 10)
    print(f"Scenario 3: -50 with 10% discount -> {price6}")
    if price6 == -45.0:
        print("  Observation: Function processes negative base price, resulting in negative final price.")
        print("  Question: Is a negative base price a valid input? The tests didn't confirm.")
    else:
        print("  Unexpected behavior for negative base price.")

    print("\n--- Conclusion ---")
    print("Even though the initial test suite passed, it didn't cover critical edge cases or business rules.")
    print("The function's behavior for these 'uncovered scenarios' was not explicitly validated,")
    print("leading to potential bugs or unexpected outcomes. This demonstrates that 'passing tests'")
    print("don't always equate to 'robust software' or comprehensive quality assurance.")

if __name__ == "__main__":
    run_tests()
