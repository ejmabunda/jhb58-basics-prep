import unittest

from calculator import add, subtract, divide, multiply, power, mod

class TestCalculator(unittest.TestCase):
    def test_calulator(self):
        # Basic operations
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(multiply(5, 7), 35)
        self.assertEqual(divide(20, 5), 4)

        self.assertEqual(add(-3, 7), 4)
        self.assertEqual(multiply(0, 4), 0)
        self.assertEqual(add(1_000_000, 2_000_000), 3_000_000)

    # Uncomment the line below if implemented
    @unittest.skip("Skipping bonus exercises for calculator")
    def test_bonuses(self):
        # Input validation
        self.assertEqual(divide(5, 0), None, "Division by is not allowed")
        self.assertEqual(add("4", 0), None, "Cannot perform addition on strings")
        self.assertEqual(subtract("4", 0), None, "Cannot perform subtraction from strings")
        self.assertEqual(divide(5, 0), None, "Cannot perform division on strings")
        self.assertEqual(multiply(5, "-2"), None, "Cannot perform multiplication on strings")
        self.assertEqual(divide(5, 0), None, "Cannot perform division on strings")

        # Power test cases
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

        # Modulus test cases
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(power(2, 5), 2)
        self.assertEqual(power(12, 4), 0)
