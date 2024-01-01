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
    def save_inventory(self):
        with open(self.inventory_filename, 'wb') as file:
            pickle.dump(self.inventory, file)
    def save_sales(self):
            with open(self.sales_filename, 'wb') as file:
                pickle.dump(self.sales, file)    
    
    def add_product(self, product):
        self.inventory.append(product)
        self.save_inventory()
        print(f'Producto "{product.name}" añadido al inventario con éxito.')
    def sell_product(self, product_id, quantity):
            for product in self.inventory:
                if product.id == product_id:
                    if product.quantity >= quantity:
                        product.quantity -= quantity
                        self.save_inventory()
                        sale = {"product_id": product.id, "quantity": quantity, "total_price": product.price * quantity}
                        self.sales.append(sale)
                        self.save_sales()
                        print(f'Venta realizada: {quantity} unidades de "{product.name}" por ${product.price * quantity}.')
                    else:
                        print(f'No hay suficientes existencias de "{product.name}" para realizar la venta.')
                    return
            print(f'Producto con ID {product_id} no encontrado en el inventario.')
    def generate_sales_report(self):
            total_sales = sum(sale["total_price"] for sale in self.sales)
            print(f'\n--- Informe de Ventas ---\nTotal de ventas: ${total_sales}\n')
