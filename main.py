import RandomBot
import InteractivePlayer
from Connect4 import Connect4, InvalidMove


def player_generator(bot1, bot2):
    round = -1
    while True:
        round += 1
        if round % 2 == 0:
            yield bot1, 'X'
        else:
            yield bot2, 'O'


def simulate_game(player1, player2):
    game = Connect4()
    pg = player_generator(player1, player2)
    while game.running:
        player, symbol = next(pg)
        game.print_board()
        move = player.next_move(game.board, symbol)
        print(f"Player {player.get_name()} plays column {move}")
        try:
            if game.play(move, symbol):
                game.print_board()
                print(f"Player {player.get_name()} won")
                return
        except InvalidMove as e:
            print(f"Player {player.get_name()} attempted an invalid move for column {move} and is disqualified")
            print(f"Player {next(pg)[0].get_name()} won")
            return

    game.print_board()
    print("Draw")
    return


def main():
    player1 = InteractivePlayer.InteractivePlayer("Human Player")
    player2 = RandomBot.RandomBot("Random Bot 2")
    simulate_game(player1, player2)


if __name__ == '__main__':
    main()

