class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initialize the product with a name, price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product. Deactivate if quantity is 0."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Check if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buy a certain quantity of the product."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.get_quantity():
            raise ValueError(f"Cannot buy {quantity} of {self.name}. Only {self.get_quantity()} in stock.")
        self.set_quantity(self.get_quantity() - quantity)
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def set_promotion(self, promotion):
        """Set a promotion for the product."""
        self.promotion = promotion

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