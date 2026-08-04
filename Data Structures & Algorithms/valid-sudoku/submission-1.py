class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                
                if not current == '.':
                    b = (r//3) * 3 + c//3

                    if current not in rows[r] and current not in cols[c] and current not in boxs[b]:
                        rows[r].add(current)
                        cols[c].add(current)
                        boxs[b].add(current)
                    else:
                        return False

        return True
