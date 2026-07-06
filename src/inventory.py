import json
from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            product.display_info()
            print("-" * 20)
    
    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def remove_product(self, product_id):
        product_to_remove = self.find_product_by_id(product_id)
        if product_to_remove:
            self.products.remove(product_to_remove)
            return True
        return False
    
    def update_product_quantity(self, product_id, new_quantity):
        product = self.find_product_by_id(product_id)
        if product:
            product.quantity = new_quantity
            return True
        return False
    
    def save_products(self):
        products_data = [product.to_dict() for product in self.products]
        with open("data/products.json", "w") as file:
            json.dump(products_data, file, indent=4)

    def load_products(self):
        try:
            with open("data/products.json", "r") as file:
                products_data = json.load(file)
                self.products = [Product.from_dict(data) for data in products_data]
        except FileNotFoundError:
            print("No products found. Starting with an empty inventory.")