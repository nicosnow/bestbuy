# main.py

# Import the necessary modules
import products
import store
import promotions

def list_products(store_instance: store.Store):
    """List all products in the store."""
    products_list = store_instance.get_all_products()
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.show()}\n")

def show_total_quantity(store_instance: store.Store):
    """Show the total quantity of all products in the store."""
    total_quantity = store_instance.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")

def get_product_from_store(store_instance, product_name):
    """Retrieve a product from the store by name."""
    return next((p for p in store_instance.get_all_products() if p.name.lower() == product_name), None)

def get_quantity_from_user():
    """Prompt the user to enter a quantity and return it."""
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return None
        return quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return None

def confirm_add_to_shopping_list(product_name, quantity):
    """Confirm with the user to add the product to the shopping list."""
    confirmation = input(f"Add {quantity} of {product_name} to the shopping list? (yes/no): ")
    return confirmation.lower() == 'yes'

def make_order(store_instance: store.Store):
    """Make an order from the store."""
    shopping_list = []
    while True:
        product_name = input("Enter product name (or 'done' to finish): ").lower()
        if product_name == 'done':
            break
        product = get_product_from_store(store_instance, product_name)
        if product:
            if product.get_quantity() == 0 and not isinstance(product, products.NonStockedProduct):
                print(f"{product_name} is out of stock.")
                continue
            quantity = get_quantity_from_user()
            if quantity is None:
                continue
            if quantity > product.get_quantity() and not isinstance(product, products.NonStockedProduct):
                print(f"Cannot order {quantity} of {product_name}. Only {product.get_quantity()} in stock.")
                continue
            if confirm_add_to_shopping_list(product_name, quantity):
                shopping_list.append((product, quantity))
                if not isinstance(product, products.NonStockedProduct):
                    product.set_quantity(product.get_quantity() - quantity)  # Temporarily reduce the stock
        else:
            print("Product not found. Please enter a valid product name.")
    try:
        total_price = store_instance.order(shopping_list)
        print(f"Total price for the order: {total_price}")
    except ValueError as error:
        print(error)

def start(store_instance: store.Store):
    """Start the store application."""
    while True:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option: ")

        if choice == '1':
            list_products(store_instance)
        elif choice == '2':
            show_total_quantity(store_instance)
        elif choice == '3':
            make_order(store_instance)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    # Start the store application
    start(best_buy)

# Call the main function
if __name__ == "__main__":
    main()