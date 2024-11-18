import unittest
from zoo import Zoo

class TestZooTicketCalculator(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negative_age(self):
        self.assertIsNone(self.zoo.get_ticket_price(-10))

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(7), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(75), 100)

if __name__ == '__main__':
    unittest.main()
