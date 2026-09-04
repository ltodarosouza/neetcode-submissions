class Solution:
    def achar(self, target, lista):
        l = 0
        r = len(lista)-1
        while l <= r:
            if lista[l] == target:
                return True
            else:
                l += 1
            if lista[r] == target:
                return True
            else:
                r -= 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            if self.achar(target, matrix[l]):
                return True
            else:
                l += 1
            if self.achar(target, matrix[r]):
                return True
            else:
                r -= 1
        return False
        