import random
from Player import Player


class RandomBot(Player):
    def next_move(self, board: list, player_symbol) -> int:
        possible_choices = []
        for i in range(7):
            if board[5][i] == '.':
                possible_choices.append(i)
        return random.choice(possible_choices)


