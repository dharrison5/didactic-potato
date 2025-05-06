import functions
import unittest
class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(functions.add(2, 3), 5)
        self.assertEqual(functions.add(-1, 1), 0)
        self.assertEqual(functions.add(0, 0), 0)
        self.assertEqual(functions.add(-5, -3), -8)

    def test_subtract(self):
        self.assertEqual(functions.subtract(5, 3), 2)
        self.assertEqual(functions.subtract(0, 1), -1)
        self.assertEqual(functions.subtract(-1, -1), 0)
        self.assertEqual(functions.subtract(10, 20), -10)

if __name__ == "__main__":
    unittest.main()