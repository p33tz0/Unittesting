import unittest
import testaus.calculator.calculator as calculator


class TestCalculatorMinus(unittest.TestCase):
    def test_minus(self):
        num1 = num2 = 2
        expected_result = 0
        result = calculator.minus(num1, num2)
        self.assertEqual(result, expected_result)

    def test_minus_works_with_floats(self):
        result = calculator.minus(2.4, 3.2)
        self.assertEqual(result, -0.8)

    def test_minus_works_with_negative_numbers(self):
        result = calculator.minus(2, -3)
        self.assertEqual(result, 5)

    def test_minus_works_with_negative_numbers_and_floats(self):
        result = calculator.minus(2.4, -3.2)
        self.assertEqual(result, 5.6)

    def test_minus_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.minus(1, "a")


class TestCalculatorJako(unittest.TestCase):
    def test_jako(self):
        num1 = num2 = 6
        expected_result = 1
        result = calculator.jako(num1, num2)
        self.assertEqual(result, expected_result)

    def test_jako_works_with_floats(self):
        result = calculator.jako(2.4, 3.2)
        self.assertEqual(result, 0.75)

    def test_jako_works_with_negative_numbers(self):
        result = calculator.jako(2, -3)
        self.assertEqual(result, -0.67)

    def test_jako_works_with_negative_numbers_and_floats(self):
        result = calculator.jako(2.4, -3.2)
        self.assertEqual(result, -0.75)

    def test_jako_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.jako(1, "a")
        
    def test_jako_numbers_takes_rises_error_if_parameters_are_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.jako(1, 0)


class TestCalculatorKertolasku(unittest.TestCase):
    def test_kertolasku(self):
        num1 = num2 = 3
        expected_result = 9
        result = calculator.kertolasku(num1, num2)
        self.assertEqual(result, expected_result)

    def test_kertolasku_works_with_floats(self):
        result = calculator.kertolasku(2.4, 3.2)
        self.assertEqual(result, 7.68)

    def test_kertolasku_works_with_negative_numbers(self):
        result = calculator.kertolasku(2, -3)
        self.assertEqual(result, -6)

    def test_kertolasku_works_with_negative_numbers_and_floats(self):
        result = calculator.kertolasku(2.4, -3.2)
        self.assertEqual(result, -7.68)

    def test_kertolasku_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(ValueError):
            calculator.kertolasku(1, "a")


class TestCalculatorPlus(unittest.TestCase):
    def test_plus(self):
        num1 = num2 = 2
        expected_result = 4
        result = calculator.plus(num1, num2)
        self.assertEqual(result, expected_result)

    def test_plus_works_with_floats(self):
        result = calculator.plus(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_plus_works_with_negative_numbers(self):
        result = calculator.plus(2, -3)
        self.assertEqual(result, -1)

    def test_plus_works_with_negative_numbers_and_floats(self):
        result = calculator.plus(2.4, -3.2)
        self.assertEqual(result, -0.8)

    def test_plus_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.plus(1, "a")


class TestCalculatorPotenssi(unittest.TestCase):
    def test_potenssi(self):
        num1 = num2 = 2
        expected_result = 4
        result = calculator.potenssi(num1, num2)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
