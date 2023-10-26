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
    def testIsosceles4(self):
        actual = Triangle.classify

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

    def testInvalidTriangleMutan1(self):
        #line20,21
        actual = Triangle.classify(-1,-10,-20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant2(self):
        #line 34,35
        actual = Triangle.classify(1,2,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant3(self):
        #line 20,21
        actual = Triangle.classify(1,-2,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant4(self):
        #line 20,21
        actual = Triangle.classify(10,10,-3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant5(self):
        #line 20,21
        actual = Triangle.classify(-10,10,-3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant6(self):
        #line 20,21
        actual = Triangle.classify(10,-10,-3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    
    def testInvalidTriangleMutant7(self):
        #line 20,21
        actual = Triangle.classify(-10,-10,3)
        expected = Triangle.Type.INVALID
    def testInvalidTriangleMutant8(self):
        #line 20,21
        actual = Triangle.classify(0,0,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant9(self):
        #line 20,21
        actual = Triangle.classify(0,2,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant10(self):
        #line 20,21
        actual = Triangle.classify(3,0,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testInvalidTriangleMutant11(self):
        #line 20,21
        actual = Triangle.classify(3,3,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)       
    def testInvalidTriangleMutant12(self):
        #line34,35
        actual = Triangle.classify(3,4,8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected) 
    def testInvalidTriangleMutant13(self):
        #line34,35
        actual = Triangle.classify(1,2,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    def testIsoscelesTriangleMutant1(self):
        #line34,35
        actual = Triangle.classify(3,3,6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual,expected)
    
    
    
    
if __name__ == '__main__':
    unittest.main()
