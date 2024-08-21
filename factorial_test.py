import unittest
from factorial import fact, div

class TestFactorial(unittest.TestCase):

    def test_fact_positive(self):
        """Test factorial with positive integers."""
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(3), 6)
    
    def test_fact_zero(self):
        """Test factorial with zero."""
        self.assertEqual(fact(0), 1)
    
    def test_fact_large(self):
        """Test factorial with a large number."""
        self.assertEqual(fact(10), 3628800)
    
    def test_fact_negative(self):
        """Test factorial with negative integers - expect ValueError."""
        with self.assertRaises(ValueError):
            fact(-1)

class TestDivision(unittest.TestCase):

    def test_div_positive(self):
        """Test division with positive integers."""
        self.assertEqual(div(2), 5.0)
        self.assertEqual(div(5), 2.0)

    def test_div_negative(self):
        """Test division with negative integers."""
        self.assertEqual(div(-2), -5.0)
        self.assertEqual(div(-5), -2.0)

    def test_div_zero(self):
        """Test division by zero - expect ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            div(0)

if __name__ == '__main__':
    unittest.main()
