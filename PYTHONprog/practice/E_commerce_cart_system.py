class Product:
    def __init__(self, name, cost, category, discount = 0):
        self.name = name
        self.cost = cost
        self.category = category
        self.discount = discount
    
    def get_discounted_price(self):
        return self.cost*(1-self.discount/100)
    
    def __str__(self):
        return f"{self.name} ({self.category}) - Rs {self.get_discounted_price():.2f}"

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product):
        self.items.append(product)
        # print(f"{product} is added to the cart.")
    
    def remove_item(self, product_name):
        self.items = [p for p in self.items if p.name != p.product_name]
        print(f"Removed {product_name} from the cart.")
    
    def calculate_total_bill(self):
        total = sum(items.get_discounted_price() for items in self.items)
        print("\nItems in the cart")
        for i in self.items:
            print(f" -{i}")
        print(f"\nThe total is Rs {total}")
        return total

iPhone = Product("iPhone", 85000, "Electronics", 10)
shoe = Product("Addidas Sambas", 10000, "Footwear", 15)
jacket = Product("Denim Jacket", 3000, "Clothing")

cart1 = Cart()
cart1.add_item(iPhone)
cart1.add_item(shoe)
cart1.add_item(jacket)

cart1.calculate_total_bill()
