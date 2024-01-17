import numpy as np

class Matrix:
    def __init__(self, N):
        self.N = N
        self.matrix = np.random.rand(N, N)  

    def inverse(self):
        return np.linalg.inv(self.matrix)

    def determinant(self):
        return np.linalg.det(self.matrix)

    def eigenvalues(self):
        return np.linalg.eigvals(self.matrix)

    def __add__(self, other):
        if self.N != other.N:
            raise ValueError("Matrices must have the same size for addition.")
        result = Matrix(self.N)
        result.matrix = self.matrix + other.matrix
        return result.matrix

    def __mul__(self, other):
        if self.N != other.N:
            raise ValueError("Matrices must have the same size for multiplication.")
        result = Matrix(self.N)
        result.matrix = np.matmul(self.matrix, other.matrix)
        return result.matrix
