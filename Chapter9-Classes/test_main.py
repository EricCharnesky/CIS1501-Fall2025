from unittest import TestCase
from main import LottoTicket
from main import Chair


class TestLottoTicket(TestCase):
    def test_is_winner(self):
        # AAA convention

        # Arrange - setup the stuff we to test
        ticket = LottoTicket(1, 2, 3)
        winning_ticket = LottoTicket(1, 2, 4)
        expected_result = False

        # Act - call the code we're testing and get results
        actual_result = ticket.is_winner(winning_ticket)

        # Assert - Did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test_is_loser(self):
        # AAA convention

        # Arrange - setup the stuff we to test
        ticket = LottoTicket(1, 2, 3)
        winning_ticket = LottoTicket(1, 2, 3)
        expected_result = True

        # Act - call the code we're testing and get results
        actual_result = ticket.is_winner(winning_ticket)

        # Assert - Did we get what we expected
        self.assertEqual(expected_result, actual_result)


class TestChair(TestCase):

    def test_init(self):
        # Arrange
        expected_color = "blue"
        expected_height = 30
        expected_has_arms = True
        expected_min_height = 10
        expected_max_height = 100

        # Act
        chair = Chair(expected_color, expected_has_arms, expected_height, expected_min_height, expected_max_height )
        actual_color = chair.get_color()
        actual_has_arms = chair.get_has_arms()
        actual_height = chair.get_height_in_cm()
        actual_min_height = chair.get_minimum_height()
        actual_max_height = chair.get_maximum_height()

        # Assert
        self.assertEqual(expected_color, actual_color)
        self.assertEqual(expected_has_arms, actual_has_arms)
        self.assertEqual(expected_height, actual_height)
        self.assertEqual(expected_min_height, actual_min_height)
        self.assertEqual(expected_max_height, actual_max_height)

    def test_change_height_works(self):
        # arrange
        chair = Chair("", False, 30, 0, 100 )
        expected_height = 40

        # act
        chair.change_height(10)
        actual_height = chair.get_height_in_cm()

        # assert
        self.assertEqual(expected_height, actual_height)

    def test_change_height_stops_at_max(self):
        # arrange
        chair = Chair("", False, 30, 0, 100 )
        expected_height = 100

        # act
        chair.change_height(1000)
        actual_height = chair.get_height_in_cm()

        # assert
        self.assertEqual(expected_height, actual_height)

    def test_change_height_stops_at_min(self):
        # arrange
        chair = Chair("", False, 30, 0, 100 )
        expected_height = 0

        # act
        chair.change_height(-1000)
        actual_height = chair.get_height_in_cm()

        # assert
        self.assertEqual(expected_height, actual_height)
