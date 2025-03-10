from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        # Check availability first
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Cannot order {quantity} of {product.name}. Only {product.get_quantity()} in stock.")

        # Process the order
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price