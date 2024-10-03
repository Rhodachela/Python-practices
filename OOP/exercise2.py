class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        total_value = self.quantity * self.price
        return total_value

product1 = Product("Sugar", 300, 3)
sum = product1.calculate_total_value()
print(f"The total value of {product1.name} in stock is {sum}")