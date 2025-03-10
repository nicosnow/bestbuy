# Import the necessary modules
import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

def start(store: store.Store):
    while True:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option: ")

        if choice == '1':
            products = store.get_all_products()
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.show()}\n")
        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total quantity in store: {total_quantity}")
        elif choice == '3':
            shopping_list = []
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input("Enter quantity: "))
                product = next((p for p in store.products if p.name == product_name), None)
                if product:
                    try:
                        shopping_list.append((product, quantity))
                    except ValueError as e:
                        print(e)
                else:
                    print("Product not found.")
            try:
                total_price = store.order(shopping_list)
                print(f"Total price for the order: {total_price}")
            except ValueError as e:
                print(e)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the start function
start(best_buy)