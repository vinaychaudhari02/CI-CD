import unittest
import math
from scientific_calculator import (
    sin_function, cos_function, tan_function, sqrt_function, log_function, exp_function,
    asin_function, acos_function, atan_function, sinh_function, cosh_function, tanh_function
)

class TestScientificCalculator(unittest.TestCase):

    # Tests for sin function
    def test_sin_positive(self):
        self.assertAlmostEqual(sin_function(90), math.sin(math.radians(90)))

    def test_sin_negative(self):
        self.assertAlmostEqual(sin_function(-90), math.sin(math.radians(-90)))

    def test_sin_zero(self):
        self.assertAlmostEqual(sin_function(0), math.sin(0))

    def test_sin_non_numeric(self):
        with self.assertRaises(ValueError):
            sin_function("hello")

    # Tests for cos function
    def test_cos_positive(self):
        self.assertAlmostEqual(cos_function(90), math.cos(math.radians(90)))

    def test_cos_negative(self):
        self.assertAlmostEqual(cos_function(-90), math.cos(math.radians(-90)))

    def test_cos_zero(self):
        self.assertAlmostEqual(cos_function(0), math.cos(0))

    def test_cos_non_numeric(self):
        with self.assertRaises(ValueError):
            cos_function("hello")

    # Tests for tan function
    def test_tan_positive(self):
        self.assertAlmostEqual(tan_function(45), math.tan(math.radians(45)))

    def test_tan_non_numeric(self):
        with self.assertRaises(ValueError):
            tan_function("hello")

    # Tests for sqrt function
    def test_sqrt_positive(self):
        self.assertEqual(sqrt_function(16), math.sqrt(16))

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt_function(-16)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(ValueError):
            sqrt_function("hello")

    # Tests for log function
    def test_log_positive(self):
        self.assertEqual(log_function(10), math.log(10))

    def test_log_non_numeric(self):
        with self.assertRaises(ValueError):
            log_function("hello")

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log_function(-10)

    # Tests for exp function
    def test_exp(self):
        self.assertEqual(exp_function(1), math.exp(1))

    def test_exp_non_numeric(self):
        with self.assertRaises(ValueError):
            exp_function("hello")

    # Tests for asin function
    def test_asin_positive(self):
        self.assertAlmostEqual(asin_function(1), math.asin(1))

    def test_asin_negative(self):
        self.assertAlmostEqual(asin_function(-1), math.asin(-1))

    def test_asin_invalid(self):
        with self.assertRaises(ValueError):
            asin_function(2)

    def test_asin_non_numeric(self):
        with self.assertRaises(ValueError):
            asin_function("hello")

    # Tests for acos function
    def test_acos_positive(self):
        self.assertAlmostEqual(acos_function(1), math.acos(1))

    def test_acos_negative(self):
        self.assertAlmostEqual(acos_function(-1), math.acos(-1))

    def test_acos_invalid(self):
        with self.assertRaises(ValueError):
            acos_function(2)

    def test_acos_non_numeric(self):
        with self.assertRaises(ValueError):
            acos_function("hello")

    # Tests for atan function
    def test_atan_positive(self):
        self.assertAlmostEqual(atan_function(1), math.atan(1))

    def test_atan_negative(self):
        self.assertAlmostEqual(atan_function(-1), math.atan(-1))

    def test_atan_non_numeric(self):
        with self.assertRaises(ValueError):
            atan_function("hello")

    # Tests for sinh function
    def test_sinh_positive(self):
        self.assertAlmostEqual(sinh_function(1), math.sinh(1))

    def test_sinh_negative(self):
        self.assertAlmostEqual(sinh_function(-1), math.sinh(-1))

    def test_sinh_non_numeric(self):
        with self.assertRaises(ValueError):
            sinh_function("hello")

    # Tests for cosh function
    def test_cosh_positive(self):
        self.assertAlmostEqual(cosh_function(1), math.cosh(1))

    def test_cosh_negative(self):
        self.assertAlmostEqual(cosh_function(-1), math.cosh(-1))

    def test_cosh_non_numeric(self):
        with self.assertRaises(ValueError):
            cosh_function("hello")

    # Tests for tanh function
    def test_tanh_positive(self):
        self.assertAlmostEqual(tanh_function(1), math.tanh(1))

    def test_tanh_negative(self):
        self.assertAlmostEqual(tanh_function(-1), math.tanh(-1))

    def test_tanh_non_numeric(self):
        with self.assertRaises(ValueError):
            tanh_function("hello")

if __name__ == '__main__':
    unittest.main()