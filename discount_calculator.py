def apply_discount(price, discount):
    # Check if price is a number (int or float)
    if type(price) not in (int, float):
        return "The price should be a number"
    
    # Check if discount is a number (int or float)
    if type(discount) not in (int, float):
        return "The discount should be a number"
    
    # Check if price is less than or equal to 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # Check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate final price after applying discount
    final_price = price - (price * (discount / 100))
    return final_price


# --- Test Cases ---
if __name__ == "__main__":
    print("Running tests...")
    print(apply_discount(100, 20))      # Expected output: 80
    print(apply_discount(200, 50))      # Expected output: 100
    print(apply_discount(74.5, 20.0))   # Expected output: 59.6
    print(apply_discount("100", 20))    # Expected output: The price should be a number
    print(apply_discount(100, -5))      # Expected output: The discount should be between 0 and 100
