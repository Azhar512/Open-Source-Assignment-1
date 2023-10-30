
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        pass

class PhysicalProduct(Product):
    def calculate_price(self):
        return self.price


class DigitalProduct(Product):
    def calculate_price(self):
        return self.price


class ShoppingCart:
    def __init__(self):
        self.cart = []

   
    def add_to_cart(self, product):
        self.cart.append(product)

   
    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print(f"{product.name} is not in the cart.")

    
    def calculate_total_price(self):
        total_price = sum(product.calculate_price() for product in self.cart)
        return total_price

    
    def checkout(self):
        total_price = self.calculate_total_price()
        print(f"Total price: ${total_price}")
        print("Checkout successful. Thank you for your purchase!")




physical_product = PhysicalProduct("Laptop", 1500)
digital_product = DigitalProduct("Ebook", 360)

cart = ShoppingCart()


cart.add_to_cart(physical_product)
cart.add_to_cart(digital_product)


total_price = cart.calculate_total_price()
print(f"Total price in the cart: ${total_price}")


cart.remove_from_cart(physical_product)


total_price = cart.calculate_total_price()
print(f"Total price in the cart after deduction: ${total_price}")


cart.checkout()
