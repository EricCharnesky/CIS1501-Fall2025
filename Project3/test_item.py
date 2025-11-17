from unittest import TestCase
from item import Item

class TestItem(TestCase):
    def test_item_string(self):
        # arrange
        expected_string = "7 bananas @ $0.30/each - $2.10"
        item = Item("bananas", 7, .3)

        # act
        actual_string = str(item)

        # assert
        self.assertEqual(expected_string, actual_string)
