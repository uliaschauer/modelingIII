class Matrix3:
    def __init__(self):
        self.elements = self.unit()

    def zero(self):
        return [[0.0 for j in range(3)] for i in range(3)]

    def unit(self):
        e = self.zero()
        for i in range(3):
            e[i][i] = 1.0
        return e

    def get_readable_string(self):
        rows = []
        for row in self.elements:
            rows.append(str(row))
        return '\n'.join(rows)

    def __str__(self):
        return self.get_readable_string()

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, item):
        return self.elements[item]

    def transpose(self):
        result = self.zero()
        for i in range(3):
            for j in range(3):
                result[j][i] += self.elements[i][j]
        return result

    def multiply(self, matrix):
        result = self.zero()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.elements[i][k] * matrix[k][j]
        return result

    def __mul__(self, matrix):
        if isinstance(matrix, Matrix3):
            return self.multiply(matrix)

    def invert(self):
        pass

    