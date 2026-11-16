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

        for i in range(0,9,3):
            for j in range(0,9,3):
                sqSeen = defaultdict(bool)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.' and board[k][l] in sqSeen and sqSeen[board[k][l]] is True:
                            return False
                        else:
                            sqSeen[board[k][l]] = True

        return True

