from .board import Board
from .players.random_player import RandomPlayer
from .players.player_level_1 import PlayerLevel1
from .player import Turn


def get_turn_report(board, player):
    player_resource = ''
    for resource, count in player.resources.items():
        player_resource += f'{resource.value}: {count} '
    return f'{player.name} - cards: {len(player.development_cards)}. points: {player.points}. resources: {player_resource}'

def play_game():
    player_achia = PlayerLevel1('achia')
    player_avigail = RandomPlayer('avigail')

    board = Board([player_achia, player_avigail])
    current_player_index = 0
    while(True):
        result = board.players[current_player_index].make_turn(board)
        if result == Turn.FAILED:
            return 'stuck'
        # print(f'\n-----\n{str(board)}')
        # print(f'\n{result}')
        board.players[current_player_index].take_noble_tiles(board)
        if board.is_final_round() and current_player_index == len(board.players) - 1:
            return board.get_winner().name
        # print(get_turn_report(board, board.players[current_player_index]))
        current_player_index = (current_player_index + 1) % len(board.players)
    # print(f'{player_achia.name}: {player_achia.points}')
    # print(f'{player_avigail.name}: {player_avigail.points}')    

def main():
    stuck = 0
    achia = 0
    avigail = 0
    tusha = 0
    itay = 0
    for index in range(1000):
        print(index)
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
    print(f'stuck: {stuck}, achia: {achia}, avigail: {avigail}, tusha: {tusha}, itay: {itay}')
    

if __name__ == "__main__":
    main()
