import unittest

from maths.matrix3 import Matrix3

class TestMatrix3(unittest.TestCase):
    
    def test_zero(self):
        matrix = Matrix3()
        matrix = matrix.zero()
        for i in range(3):
            for j in range(3):
                self.assertEqual(matrix[i][j], 0.0)

    def test_unit(self):
        matrix = Matrix3()
        matrix.unit()
        for i in range(3):
            for j in range(3):
                if i == j:
                    self.assertEqual(matrix[i][j], 1.0)
                else:
                    self.assertEqual(matrix[i][j], 0.0)

    def test_transpose(self):
        matrix = Matrix3()
        matrix[0][0] = 1.0
        matrix[0][1] = 2.0
        matrix[0][2] = 3.0
        matrix[1][0] = 4.0
        matrix[1][1] = 5.0
        matrix[1][2] = 6.0
        matrix[2][0] = 7.0
        matrix[2][1] = 8.0
        matrix[2][2] = 9.0

        transpose = matrix.transpose()

        self.assertEqual(transpose[0][0], 1.0)
        self.assertEqual(transpose[0][1], 4.0)
        self.assertEqual(transpose[0][2], 7.0)
        self.assertEqual(transpose[1][0], 2.0)
        self.assertEqual(transpose[1][1], 5.0)
        self.assertEqual(transpose[1][2], 8.0)
        self.assertEqual(transpose[2][0], 3.0)
        self.assertEqual(transpose[2][1], 6.0)
        self.assertEqual(transpose[2][2], 9.0)

    def test_invert(self):
        matrix = Matrix3()
        matrix[0][0] = 1.0
        matrix[0][1] = 2.0
        matrix[0][2] = 3.0
        matrix[1][0] = 4.0
        matrix[1][1] = 5.0
        matrix[1][2] = 6.0
        matrix[2][0] = 7.0
        matrix[2][1] = 8.0
        matrix[2][2] = 9.0

        invert = matrix.invert()
        product = matrix * invert
        
        for i in range(3):
            for j in range(3):
                if i == j:
                    self.assertEqual(product[i][j], 1.0)
                else:
                    self.assertEqual(product[i][j], 0.0)


if __name__ == '__main__':
    unittest.main()
