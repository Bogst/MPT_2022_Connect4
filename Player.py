class Player():
    def __init__(self, name):
        self.name = name

    def next_move(self, board: list, player_symbol: chr) -> int:
        raise NotImplementedError

    def get_name(self) -> str:
        return self.name
