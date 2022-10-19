from collections import Counter
from copy import deepcopy
from typing import Dict, List
from .development_card import DevelopmentCard
from .noble_tile import NobleTile
from .player import Player
from .resource import Resources
from .utils import get_all_noble_tiles, get_all_first_level_development_cards, \
                  get_all_second_level_development_cards, get_all_third_level_development_cards
from random import shuffle


GAME_OVER_POINTS = 15

class Board:
    def __init__(self, players: List[Player]) -> None:
        if len(players) > 4 or len(players) < 2:
            raise Exception('Players between 2-4')
        self.players: List[Player] = players
        self.closed_development_cards: Dict[int, List[DevelopmentCard]] = self.get_all_development_cards()
        self.opened_development_cards: Dict[int, List[DevelopmentCard]] = {}
        self.noble_tiles: List[NobleTile] = self.get_initial_noble_tiles()
        self.resources: Counter = self.get_initial_resources()
        self.init_opened_cards()

    def get_all_development_cards(self) -> Dict[int, List[DevelopmentCard]]:
        all_cards: Dict[int, List[DevelopmentCard]] = {}
        all_cards[1] = get_all_first_level_development_cards()
        all_cards[2] = get_all_second_level_development_cards()
        all_cards[3] = get_all_third_level_development_cards()
        shuffle(all_cards[1])
        shuffle(all_cards[2])
        shuffle(all_cards[3])
        return all_cards

    def init_opened_cards(self) ->  None:
        self.opened_development_cards[1] = self.closed_development_cards[1][0:4]
        self.closed_development_cards[1] = self.closed_development_cards[1][4:]
        self.opened_development_cards[2] = self.closed_development_cards[2][0:4]
        self.closed_development_cards[2] = self.closed_development_cards[2][4:]
        self.opened_development_cards[3] = self.closed_development_cards[3][0:4]
        self.closed_development_cards[3] = self.closed_development_cards[3][4:]

    def get_initial_resources(self) -> Counter:
        if len(self.players) == 2:
            return Counter({Resources.GOLD: 5, Resources.DIAMOND: 4, Resources.EMERALD: 4,
                            Resources.ONYX: 4, Resources.RUBY: 4, Resources.SAPPHIRE: 4})
        if len(self.players) == 3:
            return Counter({Resources.GOLD: 5, Resources.DIAMOND: 5, Resources.EMERALD: 5,
                            Resources.ONYX: 5, Resources.RUBY: 5, Resources.SAPPHIRE: 5})
        return Counter({Resources.GOLD: 5, Resources.DIAMOND: 7, Resources.EMERALD: 7,
                        Resources.ONYX: 7, Resources.RUBY: 7, Resources.SAPPHIRE: 7})

    def get_initial_noble_tiles(self) -> Counter:
        all_noble_tiles: List[NobleTile] = get_all_noble_tiles()
        shuffle(all_noble_tiles)
        return all_noble_tiles[:len(self.players) + 1]

    def is_final_round(self) -> bool:
        for player in self.players:
            if player.points >= GAME_OVER_POINTS:
                return True
        return False

    def get_players_results(self) -> List[Player]:
        places = deepcopy(self.players)
        places.sort(key=lambda x: x.points, reverse=True)
        detailed_places = [[places[0]]]
        current_points = places[0].points
        index = 0
        for player in places[1:]:
            if player.points == current_points:
                detailed_places[index].append(player)
                continue
            current_points = player.points
            detailed_places.append([player])
            index += 1
        results = []
        for group in detailed_places:
            group.sort(key=lambda x: len(x.development_cards), reverse=True)
            results += group
        return results

    def get_winner(self) -> Player:
        results = self.get_players_results()
        return results[0]
    
    def __str__(self) -> str:
        players = ''
        for player in self.players:
            players += f'\n\n{str(player)}'
        resources = f'yellow: {self.resources[Resources.GOLD]}, red: {self.resources[Resources.RUBY]}, blue: {self.resources[Resources.SAPPHIRE]}, green: {self.resources[Resources.EMERALD]}, white: {self.resources[Resources.DIAMOND]}, black: {self.resources[Resources.ONYX]}'
        result = f'resources: {resources}\n\n' \
                  f'players: {players}'
        return result
