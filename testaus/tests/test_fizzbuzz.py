import unittest
import testaus.Fizzbuzz.fizzbuzz as fizzbuzz


# Test that number divided by 3 returns fizz
class TestFizz(unittest.TestCase):
    def test_fizz(self):
        num1 = 6
        expected_result = "Fizz"
        result = fizzbuzz.num(num1)
        self.assertEqual(result, expected_result)


# Test that number divided by 5 returns buzz
class TestBuzz(unittest.TestCase):
    def test_buzz(self):
        num1 = 10
        expected_result = "Buzz"
        result = fizzbuzz.num(num1)
        self.assertEqual(result, expected_result)


# Test that number divided by 3 and 5 returns fizzbuzz
class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        num1 = 15
        expected_result = "FizzBuzz"
        result = fizzbuzz.num(num1)
        self.assertEqual(result, expected_result)


# Test that number not divided by 3 or 5 returns number
class TestNumber(unittest.TestCase):
    def test_number(self):
        num1 = 7
        expected_result = 7
        result = fizzbuzz.num(num1)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
