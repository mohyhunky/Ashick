
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Empty board using lists
        self.current_player = 'X'  # Human is 'X', AI is 'O'

    def print_board(self):
        print("\n".join(["|".join(row) for row in self.board]))
        print()

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_full(self):
        return ' ' not in [cell for row in self.board for cell in row]

    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                try:
                    row, col = map(int, input("Enter your move (row and column) separated by space (0-2): ").split())
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        print("Invalid input! Please enter values between 0 and 2.")
                        continue
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        if self.check_winner() or self.is_full():
                            break
                        self.current_player = 'O'
                    else:
                        print("That spot is already taken. Try again.")
                except ValueError:
                    print("Invalid input! Please enter two integers separated by a space.")
            else:
                print("AI is making a move...")
                row, col = self.best_move()
                self.board[row][col] = 'O'
                if self.check_winner() or self.is_full():
                    break
                self.current_player = 'X'

        self.print_board()
        winner = self.check_winner()
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
