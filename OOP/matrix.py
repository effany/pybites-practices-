class Matrix:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    @staticmethod
    def _to_values(obj):
        if isinstance(obj, Matrix):
            return obj.values
        if hasattr(obj, "values"):
            return obj.values
        return obj
    
    def __matmul__(self, array_b):
        right = self._to_values(array_b)
        rows_a = len(self.values)
        cols_a = len(self.values[0])
        rows_b = len(right)
        cols_b = len(right[0])

        if cols_a != rows_b:
            raise ValueError("Incompatible matrix dimensions")

        result = []
        for i in range(rows_a):
            row_result = []
            print('i', i)
            for j in range(cols_b):
                print('j', j)
                cell = 0
                for k in range(cols_a):
                    print('k', k)
                    cell += self.values[i][k] * right[k][j]
                    print(f"{self.values[i][k]} * {right[k][j]}")
                row_result.append(cell)
            result.append(row_result)
        return Matrix(result)

    def __rmatmul__(self, array_a):
        return self @ array_a

    def __imatmul__(self, array_b):
        result = self @ array_b
        self.values = result.values
        return self
    
mat1 = Matrix([[11, 12], [13, 14]])
mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(mat1 @ mat2)