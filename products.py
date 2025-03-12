# products.py

class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize the product with a name, price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def get_quantity(self):
        """Return the quantity of the product."""
        return self.quantity

    def is_active(self):
        """Check if the product is active (quantity > 0)."""
        return self.quantity > 0

    def show(self):
        """Return a string representation of the product."""
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} - ${self.price} ({self.quantity} in stock){promotion_info}"

    def set_promotion(self, promotion):
        """Set a promotion for the product."""
        self.promotion = promotion

    def buy(self, quantity):
        """Buy a certain quantity of the product."""
        if quantity > self.quantity:
            raise ValueError(f"Cannot buy {quantity} of {self.name}. Only {self.quantity} in stock.")
        self.quantity -= quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

class NonStockedProduct(Product):
    """Represents a non-stocked product in the store."""

    def __init__(self, name, price):
        """Initialize the non-stocked product with a name and price."""
        super().__init__(name, price, quantity=0)

    def get_quantity(self):
        """Return the quantity of the non-stocked product (always 0)."""
        return 0

    def is_active(self):
        """Non-stocked products are always active."""
        return True

    def show(self):
        """Return a string representation of the non-stocked product."""
        return f"{self.name} - ${self.price} (Non-stocked product)"

class LimitedProduct(Product):
    """Represents a limited product in the store."""

    def __init__(self, name, price, quantity, maximum):
        """Initialize the limited product with a name, price, quantity, and maximum purchase limit."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Buy a certain quantity of the limited product."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name} at a time.")
        return super().buy(quantity)