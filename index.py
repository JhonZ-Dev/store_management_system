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