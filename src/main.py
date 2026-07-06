from product import Product
from inventory import Inventory

def show_menu():
    print("\n=== Inventory System ===")
    print("1. List products")
    print("2. Add product")
    print("3. Find product by ID")
    print("4. Update quantity")
    print("5. Remove product")
    print("6. Save and Exit")

def main():

    inventory = Inventory()
    inventory.load_products()

    while True:
        show_menu()

        option = input("Choose an option: ")
        if option == "1":
            inventory.list_products()

        elif option == "2":
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            product_type = input("Enter product type: ")
            brand = input("Enter product brand: ")
            quantity = int(input("Enter product quantity: "))

            new_product = Product(product_id, name, product_type, brand, quantity)
            existing_product = inventory.find_product_by_id(product_id)
            if existing_product:
                print("Product with this ID already exists.")
            else:
                inventory.add_product(new_product)
                print("Product added.")
        
        elif option == "3":
            product_id = int(input("Enter product ID to find: "))
            product = inventory.find_product_by_id(product_id)
            if product:
                product.display_info()
            else:
                print("Product not found.")

        elif option == "4":
            product_id = int(input("Enter product ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            if inventory.update_product_quantity(product_id, new_quantity):
                print("Product quantity updated.")
            else:
                print("Product not found.")

        elif option == "5":
            product_id = int(input("Enter product ID to remove: "))
            if inventory.remove_product(product_id):
                print("Product removed.")
            else:
                print("Product not found.")

        elif option == "6":
            inventory.save_products()
            print("Products saved.")
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
    # print("Sistema de Inventario")

    # data = {
    #     "product_id": 99,
    #     "name": "MacBook Air",
    #     "product_type": "Laptop",
    #     "brand": "Apple",
    #     "quantity": 3
    # }

    # product = Product.from_dict(data)
    # # product.display_info()

    # inventory = Inventory()

    # inventory.load_products()
    # inventory.list_products()

    # laptop = Product(
    #     1,
    #     "ThinkPad E14",
    #     "Laptop",
    #     "Lenovo",
    #     10
    # )

    # printer = Product(
    #     2,
    #     "LaserJet Pro",
    #     "Printer",
    #     "HP",
    #     5
    # )

    # inventory.add_product(laptop)
    # inventory.add_product(printer)

    # inventory.save_products()

    # print("Products saved.")

    # if inventory.remove_product(1):
    #     print("Product removed.")
    # else:
    #     print("Product not found.")

    # if inventory.update_product_quantity(2, 8):
    #     print("Product quantity updated.")
    # else:
    #     print("Product not found.")

    # inventory.list_products()

    # product = inventory.find_product_by_id(1)

    # if product:
    #     product.display_info()
    # else:
    #     print("Product not found.")

if __name__ == "__main__":
    main()

