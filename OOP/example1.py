import unittest
def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        result = add(6, 9)
        self.assertEqual(result, 15)    
    def test_add_negative(self):
        result = add(-5, 7)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()