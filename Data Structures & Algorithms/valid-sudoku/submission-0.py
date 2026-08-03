class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for c in range(9):
            for r in range(9):
                current = board[c][r]

                current_box  = (r // 3) * 3 + (c // 3)

                if current in rows[r] or current in columns[c] or current in boxes[current_box]:
                    return False

                if not current == '.':
                    rows[r].add(current)
                    columns[c].add(current)
                    boxes[current_box].add(current)

        return True
        