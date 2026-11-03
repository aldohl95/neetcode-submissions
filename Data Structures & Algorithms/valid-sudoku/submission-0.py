class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == ".":
                    continue
                if value in rows[i]:
                    return False
                if value in columns[j]:
                    return False
                if value in squares[i//3,j//3]:
                    return False
                rows[i].add(value)
                columns[j].add(value)
                squares[i//3,j//3].add(value)
        return True