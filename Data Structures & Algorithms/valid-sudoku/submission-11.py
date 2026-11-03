class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenColumn = defaultdict(set)
        seenSquare = defaultdict(set)

        for c in range(len(board)):
            for r in range(len(board[c])):
                if board[c][r] == ".":
                    continue
                if (board[c][r] in seenColumn[c] or board [c][r] in seenRow[r] or board[c][r] in seenSquare[(c//3,r//3)]):
                    return False
                seenColumn[c].add(board[c][r])
                seenRow[r].add(board[c][r])
                seenSquare[(c//3, r//3)].add(board[c][r])
        return True

        