import unittest

from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("1,5"), 6)
    
    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3,4,5"), 15)
    
    def test_new_line_as_delimiter(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)

    def test_mulitple_delimiters(self):
        self.assertEqual(StringCalculator.add("//abc\n1abc3abc4"), 8)

    def test_mixed_delimiters(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator.add("//;\n1;2,3")
        self.assertEqual(str(context.exception), "invalid input, mixed delimiters not allowed")
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2, -4")

if __name__ == "__main__":
    unittest.main()