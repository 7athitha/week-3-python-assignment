def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

    # user's input on original price and discount percentage
try:
    original_price = input("Enter the original price of the item: ").strip()
    discount = input("Enter the discount percentage: ").strip()

    # validate and convert inputs to floats
    if original_price.replace(".", "", 1).isdigit() and discount.replace(".", "", 1).isdigit():
        original_price = float(original_price)  
        discount = float(discount)  

        final_price = calculate_discount(original_price, discount)

    # c21heck if the discount was applied and print the appropriate message
        if final_price == original_price:
            print(f"No discount was applied. The original price is: R{original_price:.2f}")
        else:
            print(f"The final price after applying the discount is: R{final_price:.2f}")
    else:
        print("Invalid input. Please enter numeric values for the price and discount percentage.")
except ValueError:
    print("Invalid input. Please enter valid numbers for the price and discount percentage.")