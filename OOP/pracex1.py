import unittest
number = int(input("Enter the number: "))
def calculation(num):
    square = num **2
    return square

class TestSquare(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(calculation(2), 4)
        self.assertEqual(calculation(3), 9)
    def test_negative_input(self):
        self.assertEqual(calculation(-4), 16)
    def test_zero_input(self):
        self.assertEqual(calculation(0), 0)
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculation("Invalid")

if __name__ == "__main__":
    unittest.main()