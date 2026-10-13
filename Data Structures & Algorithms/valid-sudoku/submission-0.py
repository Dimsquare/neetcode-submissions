from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current==".":
                    continue
                elif current in rows.keys():
                    return False
                else:
                    rows[current] = row
                if current in cols[col]:
                    return False
                cols[col].add(current)
                square = ((row//3)*3)+(col//3)
                if current in boxes[square]:
                    return False
                boxes[square].add(current)
            rows={}

        return True
