class Product:
    def __init__(self, product_id, name, product_type, brand, quantity):
        self.product_id = product_id
        self.name = name
        self.product_type = product_type
        self.brand = brand
        self.quantity = quantity

    def display_info(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.product_type}")
        print(f"Brand: {self.brand}")
        print(f"Quantity: {self.quantity}")
    
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "product_type": self.product_type,
            "brand": self.brand,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["product_type"],
            data["brand"],
            data["quantity"]
        )