def calculate_subtotal(items):
    """Calculates the subtotal by summing up total price of each item."""
    subtotal = 0.0
    for item in items:
        subtotal += item['quantity'] * item['price']
    return subtotal

def calculate_discount(subtotal, discount_percentage=10.0):
    """Calculates the discount amount based on a percentage."""
    return subtotal * (discount_percentage / 100)

def calculate_tax(amount_after_discount, tax_percentage=5.0):
    """Calculates the tax amount based on a percentage."""
    return amount_after_discount * (tax_percentage / 100)

def generate_bill(items, discount_pct=10.0, tax_pct=5.0):
    """Generates and prints a cleanly formatted itemized bill."""
    print("\n" + "="*45)
    print(f"{'SHOPPING BILL':^45}")
    print("="*45)
    print(f"{'Item Name':<15} {'Qty':<5} {'Price':<10} {'Total':<10}")
    print("-"*45)
    
    # Print each itemized row
    for item in items:
        item_total = item['quantity'] * item['price']
        print(f"{item['name']:<15} {item['quantity']:<5} ${item['price']:<9.2f} ${item_total:<10.2f}")
        
    print("-"*45)
    
    # Perform calculations using functions
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, discount_pct)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_pct)
    final_total = taxable_amount + tax
    
    # Print final totals formatted to 2 decimal places
    print(f"{'Subtotal:':<32} ${subtotal:>10.2f}")
    print(f"{f'Discount ({discount_pct}%):':<32} -${discount:>9.2f}")
    print(f"{f'Tax ({tax_pct}%):':<32} +${tax:>9.2f}")
    print("="*45)
    print(f"{'Final Total:':<32} ${final_total:>10.2f}")
    print("="*45)

def main():
    # List to store product records as dictionaries (Structured Data)
    shopping_cart = []
    
    print("Welcome to the Shopping Bill Generator!")
    print("Enter item details below. Type 'done' as item name to finish.\n")
    
    while True:
        name = input("Enter product name: ").strip()
        if name.lower() == 'done':
            break
        if not name:
            print("Product name cannot be empty. Try again.")
            continue
            
        # Validation for input quantities and prices
        try:
            quantity = int(input(f"Enter quantity for {name}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero. Try again.")
                continue
                
            price = float(input(f"Enter price for {name}: $"))
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers for quantity and price.")
            continue
            
        # Storing data dynamically in a structured dictionary
        product = {
            'name': name,
            'quantity': quantity,
            'price': price
        }
        shopping_cart.append(product)
        print(f"-> {name} added to cart.\n")
        
    if shopping_cart:
        # Generate final output
        generate_bill(shopping_cart, discount_pct=10.0, tax_pct=5.0)
    else:
        print("\nNo items were added. Cart is empty.")

if __name__ == "__main__":
    main()