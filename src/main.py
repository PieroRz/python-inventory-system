from product import Product
from inventory import Inventory


def main():
    print("Sistema de Inventario")

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

    product = inventory.find_product_by_id(2)

    if product:
        product.display_info()
    else:
        print("Product not found.")


if __name__ == "__main__":
    main()

