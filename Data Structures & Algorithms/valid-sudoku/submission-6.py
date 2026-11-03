class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenrow = defaultdict(set)
        seenCol = defaultdict(set)
        seenSquare = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if(board[i][j] in seenrow[i] or board[i][j] in seenCol[j] or board[i][j] in seenSquare[(i//3, j//3)]):
                    return False
            
                seenrow[i].add(board[i][j])
                seenCol[j].add(board[i][j])
                seenSquare[(i//3, j//3)].add(board[i][j])
        return True