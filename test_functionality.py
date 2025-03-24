# test_functionality.py
import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store

def test_order_limited_product_over_limit():
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(2)

def test_percent_discount_promotion():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = PercentDiscount(name="30% off", percent=30)
    product.set_promotion(promotion)
    total_price = product.buy(2)
    assert total_price == 140  # 30% off on 2 items

def test_second_half_price_promotion():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice(name="Second Half Price")
    product.set_promotion(promotion)
    total_price = product.buy(3)
    assert total_price == 250  # 2 full price + 1 half price

def test_third_one_free_promotion():
    product = Product(name="Test Product", price=100, quantity=10)
    promotion = ThirdOneFree(name="Third One Free")
    product.set_promotion(promotion)
    total_price = product.buy(4)
    assert total_price == 300  # 3 full price + 1 free

def test_store_initialization_with_invalid_product():
    with pytest.raises(TypeError):
        Store(product_list=["Invalid Product"])

def test_store_add_invalid_product():
    store = Store(product_list=[])
    with pytest.raises(TypeError):
        store.add_product("Invalid Product")

def test_store_order():
    product1 = Product(name="Product 1", price=50, quantity=5)
    product2 = Product(name="Product 2", price=30, quantity=3)
    store = Store(product_list=[product1, product2])
    shopping_list = [(product1, 2), (product2, 1)]
    total_price = store.order(shopping_list)
    assert total_price == 130  # 2 * 50 + 1 * 30