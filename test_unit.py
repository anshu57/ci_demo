import unittest
from example import add, mul

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(1, 10), 11)
    

    def test_mul(self):
        self.assertEqual(mul(10, 2), 20)
        self.assertEqual(mul(3, 10), 30)

if __name__=='__main__':
    unittest.main()