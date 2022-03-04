class InvalidMove(Exception):
    pass


class Connect4:
    def __init__(self):
        self.board = [['.' for _ in range(7)] for _ in range(6)]
        self.running = True

    def play(self, move: int, symbol: chr) -> bool:
        # if self.board
        if type(move) is not int or move < 0:
            self.running = False
            raise InvalidMove
        row = 0
        try:
            while self.board[row][move] != '.':
                row += 1
            self.board[row][move] = symbol
        except (IndexError, TypeError):
            self.running = False
            raise InvalidMove

        # check if game was won

        # check there are still positions to play

        # check horizontal
        win = False
        for i in range(6):
            for j in range(4):
                win = win or (self.board[i][j]     == symbol and
                              self.board[i][j + 1] == symbol and
                              self.board[i][j + 2] == symbol and
                              self.board[i][j + 3] == symbol)

        # check vertical
        for i in range(3):
            for j in range(7):
                win = win or (self.board[i][j]     == symbol and
                              self.board[i + 1][j] == symbol and
                              self.board[i + 2][j] == symbol and
                              self.board[i + 3][j] == symbol)

        # check diagonal
        for i in range(3):
            for j in range(4):
                win = win or (self.board[i][j]         == symbol and
                              self.board[i + 1][j + 1] == symbol and
                              self.board[i + 2][j + 2] == symbol and
                              self.board[i + 3][j + 3] == symbol)

        # check other diagonal
        for i in range(3):
            for j in range(3,7):
                win = win or (self.board[i][j]         == symbol and
                              self.board[i + 1][j - 1] == symbol and
                              self.board[i + 2][j - 2] == symbol and
                              self.board[i + 3][j - 3] == symbol)

        if win:
            return True

        free_positions = False
        for i in range(7):
            free_positions = free_positions or self.board[5][i] == "."

        if not free_positions:
            self.running = False

        return False

    def print_board(self):
        for i in range(5, -1, -1):
            for j in range(7):
                print(f"|{self.board[i][j]}|", end=" ")
            print("")
