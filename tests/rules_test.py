from src.board import Board
from src.players.random_player import RandomPlayer
from src.player import Turn


def play_game():
    player_achia = RandomPlayer('achia')
    player_avigail = RandomPlayer('avigail')
    # player_tusha = RandomPlayer('tusha')
    # player_itay = RandomPlayer('itay')
    board = Board([player_achia, player_avigail])
    current_player_index = 0
    while(True):
        result = board.players[current_player_index].make_turn(board)
        if result == Turn.FAILED:
            return 'stuck'
        
        board.players[current_player_index].take_noble_tiles(board)
        if board.is_final_round() and current_player_index == len(board.players) - 1:
            return board.get_winner().name
        current_player_index = (current_player_index + 1) % len(board.players)


def test_rules():
    stuck = 0
    achia = 0
    avigail = 0
    tusha = 0
    itay = 0
    for index in range(1000):
        result = play_game()
        if result == 'stuck':
            stuck += 1
        if result == 'achia':
            achia += 1
        if result == 'avigail':
            avigail += 1
        if result == 'tusha':
            tusha += 1
        if result == 'itay':
            itay += 1
