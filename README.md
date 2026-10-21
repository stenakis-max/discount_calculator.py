# Discount Calculator (Python Challenge)

A simple Python function that calculates the final price of a product after applying a percentage discount, featuring strict input validation.

## Features & Validations

The function `apply_discount(price, discount)` ensures data integrity by performing the following checks before any calculation:
- **Type Checking:** Verifies that both `price` and `discount` are numbers (`int` or `float`).
- **Value Bounds:** 
  - Ensures the `price` is strictly greater than `0`.
  - Ensures the `discount` percentage is between `0` and `100` (inclusive).

If any check fails, it returns a specific, user-friendly error message instead of crashing.

## Usage

You can import and use the function in your Python scripts as follows:

```python
from discount_calculator import apply_discount

# Valid inputs
print(apply_discount(100, 20))      # Output: 80
print(apply_discount(74.5, 20.0))   # Output: 59.6

# Invalid inputs
print(apply_discount("100", 20))    # Output: "The price should be a number"
print(apply_discount(100, 150))     # Output: "The discount should be between 0 and 100"
```
