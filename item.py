class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('name'={self.name}, 'price'={self.price}, 'quantity'={self.quantity})"

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate
