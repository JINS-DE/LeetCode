class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str: 
        board = [[""] * 3 for _ in range(3)]

        def check_winner(player, row, col):
            return(
                all(board[row][c] == player for c in range(3)) or
                all(board[r][col] == player for r in range(3)) or
                (row==col and all(board[k][k] == player for k in range(3))) or
                (row+col==2 and all(board[k][2-k]==player for k in range(3)))
            )

        for i,(row,col) in enumerate(moves):
            player = "X" if i%2==0 else "O"
            board[row][col] = player
            if check_winner(player,row,col):
                return "A" if player=="X" else "B"

        return "Draw" if len(moves) == 9 else "Pending"