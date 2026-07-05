def main():
    print("Sistema de Inventario")

if __name__ == "__main__":
    main()

from product import Product
from inventory import Inventory

inventory = Inventory()

laptop = Product(
    1,
    "ThinkPad E14",
    "Laptop",
    "Lenovo",
    10
)

printer = Product(
    2,
    "LaserJet Pro",
    "Printer",
    "HP",
    5
)

inventory.add_product(laptop)
inventory.add_product(printer)

inventory.list_products()

