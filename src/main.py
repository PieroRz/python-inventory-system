def main():
    print("Sistema de Inventario")

if __name__ == "__main__":
    main()

from product import Product

laptop = Product(
    1,
    "ThinkPad E14",
    "Laptop",
    "Lenovo",
    10
)

laptop.display_info()