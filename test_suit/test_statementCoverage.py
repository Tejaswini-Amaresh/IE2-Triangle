import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def testEquilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(10, 11, 12)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def testIsosceles1(self):
        actual = Triangle.classify(10, 10, 12)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def testIsosceles2(self):
        actual = Triangle.classify(10, 12, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def testIsosceles3(self):
        actual = Triangle.classify(12, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testInvalid(self):
        actual = Triangle.classify(-10, 10, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testViolateInequality(self):
        actual = Triangle.classify(10, 5, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testViolateInequalityIsos1(self):
        actual = Triangle.classify(10, 10, 25)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testViolateInequalityIsos2(self):
        actual = Triangle.classify(10, 25, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testViolateInequalityIsos3(self):
        actual = Triangle.classify(25, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
