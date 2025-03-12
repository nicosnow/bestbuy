# test_promotions.py

import pytest
from products import Product
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

def test_percent_discount():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = PercentDiscount(name="30% off", percent=30)
    product.set_promotion(promotion)
    total_price = product.buy(2)
    assert total_price == 140  # 30% off on 2 items

def test_second_half_price():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice(name="Second Half Price")
    product.set_promotion(promotion)
    total_price = product.buy(3)
    assert total_price == 250  # 2 full price + 1 half price

def test_third_one_free():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = ThirdOneFree(name="Third One Free")
    product.set_promotion(promotion)
    total_price = product.buy(4)
    assert total_price == 300  # 3 full price + 1 free

def test_no_promotion():
    product = Product(name="Test Product", price=100, quantity=10)
    total_price = product.buy(2)
    assert total_price == 200  # No promotion applied