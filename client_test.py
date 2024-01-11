import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2,
                ),
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2,
                ),
            )


class TestGetRatioFunction(unittest.TestCase):
    def test_valid_ratio(self):
        """Test with valid prices."""
        self.assertAlmostEqual(getRatio(10, 5), 2.0)

    def test_zero_denominator(self):
        """Test when price_b (denominator) is zero."""
        self.assertIsNone(getRatio(10, 0))

    def test_negative_values(self):
        """Test with negative values."""
        self.assertAlmostEqual(getRatio(-10, 5), -2.0)

    def test_fractional_values(self):
        """Test with fractional values."""
        self.assertAlmostEqual(getRatio(1, 3), 1 / 3)

    def test_both_values_zero(self):
        """Test when both price_a and price_b are zero."""
        self.assertIsNone(getRatio(0, 0))


if __name__ == "__main__":
    unittest.main()
