class Item:

    def __init__(self, name, quantity, unit_price):
        self._name = name
        self.set_quantity(quantity)
        self.set_unit_price(unit_price)

    def set_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid Quantity")
        self._quantity = quantity

    def set_unit_price(self, unit_price):
        if unit_price <= 0:
            raise ValueError("Invalid unit price")
        self._unit_price = unit_price

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_unit_price(self):
        return self._unit_price

    def get_total_price(self):
        return self._unit_price * self._quantity

    def __str__(self):
        return f'{self._quantity} {self._name} @ ${self._unit_price:.2f}/each - ${self.get_total_price():.2f}'