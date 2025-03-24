# test_product.py

import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_create_normal_product():
    product = Product(name="Test Product", price=100, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 10

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product(name="", price=100, quantity=10)
    with pytest.raises(ValueError):
        Product(name="Test Product", price=-100, quantity=10)
    with pytest.raises(ValueError):
        Product(name="Test Product", price=100, quantity=-10)

def test_product_purchase_modifies_quantity_and_returns_output():
    product = Product(name="Test Product", price=100, quantity=10)
    total_price = product.buy(3)
    assert product.quantity == 7
    assert total_price == 300

def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product(name="Test Product", price=100, quantity=10)
    with pytest.raises(ValueError):
        product.buy(15)

def test_create_non_stocked_product():
    product = NonStockedProduct(name="Windows License", price=125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.get_quantity() == 0
    assert product.is_active()

def test_create_limited_product():
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1

def test_non_stocked_product_always_active():
    product = NonStockedProduct(name="Windows License", price=125)
    assert product.is_active()

def test_limited_product_purchase_within_limit():
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    total_price = product.buy(1)
    assert product.quantity == 249
    assert total_price == 10

def test_limited_product_purchase_exceeds_limit():
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(2)