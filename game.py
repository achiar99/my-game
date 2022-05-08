from board import Board
from players.random_player import RandomPlayer


def get_turn_report(board, player):
    player_resource = ''
    for resource, count in player.resources.items():
        player_resource += f'{resource.value}: {count} '
    return f'{player.name} - cards: {len(player.development_cards)}. points: {player.points}. resources: {player_resource}'

def play_game():
    player_achia = RandomPlayer('achia')
    player_avigail = RandomPlayer('avigail')
    player_tusha = RandomPlayer('tusha')
    player_itay = RandomPlayer('itay')
    board = Board([player_achia, player_avigail, player_tusha, player_itay])
    current_player_index = 0
    while(True):
        success = board.players[current_player_index].make_turn(board)
        if not success:
            # print(f'stuck')
            return 'stuck'
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
