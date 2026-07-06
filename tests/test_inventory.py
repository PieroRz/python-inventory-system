import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from inventory import Inventory
from product import Product

def test_add_product():
    inventory = Inventory()

    product = Product(
        1,
        "ThinkPad E14",
        "Laptop",
        "Lenovo",
        10
    )

    inventory.add_product(product)

    assert len(inventory.products) == 1

def test_find_product_by_id():
    inventory = Inventory()

    product = Product(
        1,
        "ThinkPad E14",
        "Laptop",
        "Lenovo",
        10
    )

    inventory.add_product(product)

    result = inventory.find_product_by_id(1)

    assert result is not None
    assert result.name == "ThinkPad E14"

def test_remove_product():
    inventory = Inventory()

    product = Product(
        1,
        "ThinkPad E14",
        "Laptop",
        "Lenovo",
        10
    )

    inventory.add_product(product)

    result = inventory.remove_product(1)

    assert result is True
    assert len(inventory.products) == 0

def test_update_product_quantity():
    inventory = Inventory()

    product = Product(
        1,
        "ThinkPad E14",
        "Laptop",
        "Lenovo",
        10
    )

    inventory.add_product(product)

    inventory.update_product_quantity(1, 20)

    assert product.quantity == 20