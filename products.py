# products.py

class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize the product with a name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        """Return the quantity of the product."""
        return self.quantity

    def is_active(self):
        """Check if the product is active (quantity > 0)."""
        return self.quantity > 0

    def show(self):
        """Return a string representation of the product."""
        return f"{self.name} - ${self.price} ({self.quantity} in stock)"

    def buy(self, quantity):
        """Buy a certain quantity of the product."""
        if quantity > self.quantity:
            raise ValueError(f"Cannot buy {quantity} of {self.name}. Only {self.quantity} in stock.")
        self.quantity -= quantity
        return self.price * quantity