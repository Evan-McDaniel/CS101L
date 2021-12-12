import unittest
import grades
import math

class GradeTest(unittest.TestCase):

    def test_total_returns_total(self):
        total = grades.total([1,5,9])
        self.assertEqual(total,15,'should be 15')
    def test_total_returns_zero(self):
        total = grades.total([])
        self.assertEqual(total,0,'Should be 0')

    def test_average_one(self):
        result = grades.average([2,9,5])
        self.assertAlmostEqual(result,5.3333,3)
    def test_average_two(self):
        result = grades.average([2,15,22,9])
        self.assertAlmostEqual(12.0000,result,5)
    def test_average_returns_nan(self):
        result = grades.average([])
        self.assertIs(result,math.nan)
    
    def test_median_one(self):
        test = grades.median([2,5,1])
        self.assertEqual(test,2)
    def test_median_two(self):
        test = grades.median([2,5,1,3])
        self.assertEqual(test,2.5)
    def test_median_error(self):
        with self.assertRaises(ValueError):
            grades.median([])

unittest.main()