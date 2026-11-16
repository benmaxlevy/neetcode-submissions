class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        # checking columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])

        seen = defaultdict(bool)
        squares = [
            [
                [0,2],
                [0,2]
            ],
            [
                [0,2],
                [3,5]
            ],
            [
                [0,2],
                [6,8]
            ],
            [
                [3,5],
                [0,2]
            ],
            [
                [3,5],
                [3,5]
            ],
            [
                [3,5],
                [6,8]
            ],
            [
                [6,8],
                [0,2]
            ],
            [
                [6,8],
                [3,5]
            ],
            [
                [6,8],
                [6,8]
            ],
        ]

        for square in squares:
            sqSeen = defaultdict(bool)
            for i in range(square[0][0], square[0][1] + 1):
                for j in range(square[1][0], square[1][1] + 1):
                    if board[i][j] != '.' and board[i][j] in sqSeen and sqSeen[board[i][j]] is True:
                        return False
                    else:
                        sqSeen[board[i][j]] = True

        return True

