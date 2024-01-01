import os
import pickle

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
class StoreManager:
    def __init__(self, inventory_filename="inventory.pkl", sales_filename="sales.pkl"):
        self.inventory_filename = inventory_filename
        self.sales_filename = sales_filename
        self.inventory = self.load_inventory()
        self.sales = self.load_sales()
    def load_inventory(self):
        if os.path.exists(self.inventory_filename):
            with open(self.inventory_filename, 'rb') as file:
                return pickle.load(file)
        return []
    def load_sales(self):
        if os.path.exists(self.sales_filename):
            with open(self.sales_filename, 'rb') as file:
                return pickle.load(file)
        return []