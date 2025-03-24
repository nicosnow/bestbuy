# store.py

import products  # Add this import statement

class Store:
    """Represents a store with a list of products."""

    def __init__(self, product_list):
        """Initialize the store with a list of products."""
        for product in product_list:
            if not isinstance(product, products.Product):
                raise TypeError("All items in the product list must be instances of the Product class.")
        self.products = product_list

    def add_product(self, product):
        """Add a product to the store."""
        if not isinstance(product, products.Product):
            raise TypeError("The product must be an instance of the Product class.")
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Place an order for a list of products and quantities."""
        # Check availability first
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Cannot order {quantity} of {product.name}. Only {product.get_quantity()} in stock.")

        # Process the order
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price