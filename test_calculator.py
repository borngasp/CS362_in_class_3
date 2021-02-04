import unittest
import calculator


class CalculatorTestCases(unittest.TestCase):

    def test_add(self):
        result = calculator.add(2,4)
        self.assertEqual(result, 6)

    def test_sub(self):
        self.assertEqual(calculator.sub(4,2), 2)

    def test_mul(self):
        self.assertEqual(calculator.mul(2,4), 8)

    def test_div(self):
        self.assertEqual(calculator.div(16,4), 4)

if __name__ == "__main__":
    unittest.main()

