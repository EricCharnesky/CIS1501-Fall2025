from typing import overload, override

from item import Item

class TaxableItem(Item):

    def __init__(self, name, quantity, unit_price, tax_rate):
        super().__init__(name, quantity, unit_price)
        self.set_tax_rate(tax_rate)

    def set_tax_rate(self, tax_rate):
        if tax_rate > 1:
            tax_rate /= 100
        self._tax_rate = tax_rate

    def get_tax_rate(self):
        return self._tax_rate

    @override
    def get_total_price(self):
        return super().get_total_price() * ( 1 + self._tax_rate )
        # return self._quantity * self.get_unit_price() * ( 1 + self._tax_rate )