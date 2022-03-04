from Player import Player


class InteractivePlayer(Player):
    def next_move(self, board: list, player_symbol: chr) -> int:
        print(f"You are {player_symbol}")

        for i in range(5, -1, -1):
            for j in range(7):
                print(f"|{board[i][j]}|", end=" ")
            print("")

        return int(input("In what column do you want to play[0 index column]"))