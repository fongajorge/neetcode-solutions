class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (cols * rows) - 1

        while l <= r:
            m = (l + r) // 2
            m_row = m // cols
            m_col = m % cols

            if target == matrix[m_row][m_col]:
                return True
            elif target < matrix[m_row][m_col]:
                r = m - 1
            else:
                l = m + 1   

        return False
        