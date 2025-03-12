# promotions.py

from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Apply the promotion to the given product and quantity."""
        pass

class PercentDiscount(Promotion):
    """Promotion for a percentage discount."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity

class SecondHalfPrice(Promotion):
    """Promotion for second item at half price."""

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class ThirdOneFree(Promotion):
    """Promotion for buy 2, get 1 free."""

    def apply_promotion(self, product, quantity):
        full_price_items = (quantity // 3) * 2 + quantity % 3
        return full_price_items * product.price