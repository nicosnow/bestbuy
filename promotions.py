from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price
        discounted_price = product.price - discount
        return discounted_price * quantity

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity // 2 + quantity % 2
        half_price_quantity = quantity // 2
        return full_price_quantity * product.price + half_price_quantity * (product.price / 2)

class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity - (quantity // 3)
        return full_price_quantity * product.price