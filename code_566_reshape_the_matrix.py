import numpy
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        return numpy.reshape(mat, (r,c)) if n*m == r*c else mat