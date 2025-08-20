def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount

        return final_price
    else:
        
        return price
try:
    original_price = float(input("Enter the original price of the item\n"))
    discount_percent = float(input("Enter the discount percent\n"))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after applying the discount is\n {final_price}")
    else:
        print(f"No discount applied. The  price is\n {original_price}")
except ValueError:
    print("Please enter valid numeric values for price and discount percent.")