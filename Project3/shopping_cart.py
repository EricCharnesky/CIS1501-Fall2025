from item import Item

class ShoppingCart:

    def __init__(self):
        self._items = []

    def add_item(self, item : Item):
        self._items.append(item)

    def receipt(self):
        total = 0
        result = ""
        for item in self._items:
            result += str(item) + "\n"
            total += item.get_total_price()
        result += f"Grand Total: ${total:.2f}"
        return result