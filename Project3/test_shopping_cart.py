from unittest import TestCase

from shopping_cart import ShoppingCart
from item import Item

class TestShoppingCart(TestCase):
    def test_receipt(self):
        # arrange
        cart = ShoppingCart()
        cart.add_item(Item("bananas", 7, .3))
        cart.add_item(Item("Coffee", 3, 2.99))
        expected_receipt = """7 bananas @ $0.30/each - $2.10
3 Coffee @ $2.99/each - $8.97
Grand Total: $11.07"""

        # act
        actual_receipt = cart.receipt()

        # assert
        self.assertEqual(expected_receipt, actual_receipt)