# test_product.py

import pytest
from products import Product

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

def test_product_becomes_inactive_when_quantity_zero():
    product = Product(name="Test Product", price=100, quantity=0)
    assert not product.is_active()

def test_product_purchase_modifies_quantity_and_returns_output():
    product = Product(name="Test Product", price=100, quantity=10)
    total_price = product.buy(3)
    assert product.quantity == 7
    assert total_price == 300

def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product(name="Test Product", price=100, quantity=10)
    with pytest.raises(ValueError):
        product.buy(15)