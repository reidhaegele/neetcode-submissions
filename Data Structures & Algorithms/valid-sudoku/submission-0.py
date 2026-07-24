class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(len(board))]
        squares = [[set(), set(), set()] for _ in range(3)]
        for row in range(len(board)):
            across = set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in cols[col]:
                    return False
                cols[col].add(board[row][col])
                if board[row][col] in across:
                    return False
                across.add(board[row][col])
                if board[row][col] in squares[row//3][col//3]:
                    return False
                squares[row//3][col//3].add(board[row][col])


        return True

