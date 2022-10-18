from __future__ import annotations
import random
from typing import Counter, List, Optional
from ..noble_tile import NobleTile
from ..development_card import DevelopmentCard
from ..resource import Resources
from ..player import Player, Turn
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from board import Board

class RandomPlayer(Player):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.development_cards_in_hand: List[DevelopmentCard] = []
        self.development_cards: List[DevelopmentCard] = []
        self.resources: Counter = Counter({Resources.GOLD: 0, Resources.DIAMOND: 0, Resources.EMERALD: 0,
                                           Resources.ONYX: 0, Resources.RUBY: 0, Resources.SAPPHIRE: 0})
        self.noble_tiles: List[NobleTile] = []

    def needs_take_three_resources(self, board: Board) -> Optional[List[Resources]]:
        result: List[Resources] = []
        resources = [Resources.DIAMOND, Resources.EMERALD, Resources.ONYX, Resources.RUBY, Resources.SAPPHIRE]
        counter = 0
        while (resources and counter < 5 and len(result) < 3):
            random_resource = random.choice(resources)
            if board.resources[random_resource] > 0:
                resources.remove(random_resource)
                result.append(random_resource)
            counter += 1
        return result

    def needs_take_two_resources(self, board: Board) -> Optional[Resources]:
        resources = [Resources.DIAMOND, Resources.EMERALD, Resources.ONYX, Resources.RUBY, Resources.SAPPHIRE]
        counter = 0
        while (counter < 5):
            random_resource = random.choice(resources)
            if board.resources[random_resource] >= 4:
                return random_resource
            counter += 1
        return None

    def needs_take_gold_and_card(self, board: Board) -> Optional[Resources]:
        if len(board.closed_development_cards[1]) == 0 and len(board.closed_development_cards[2]) == 0 and len(board.closed_development_cards[3]) == 0:
            return False
        return board.resources[Resources.GOLD] > 0 and len(self.development_cards_in_hand) < 3

    def can_buy_card(self, card: DevelopmentCard) -> bool:
        missing = 0
        discount = self.get_discount()
        for resource, count in card.cost.items():
            if count == 0:
                continue
            if self.resources[resource] + discount[resource] < count:
                missing += count - self.resources[resource]
        if missing == 0:
            return True
        if self.resources[Resources.GOLD] >= missing:
            return True
        return False

    def needs_to_buy_card(self, board: Board) -> Optional[DevelopmentCard]:
        def needs_to_buy_card_in_level(level: int):
            for card in [card for card in self.development_cards_in_hand if card.level == level]:
                if self.can_buy_card(card):
                    return card
            for card in board.opened_development_cards[level]:
                if self.can_buy_card(card):
                    return card
            return None
        
        card = needs_to_buy_card_in_level(3)
        if card:
            return card
        card = needs_to_buy_card_in_level(2)
        if card:
            return card
        card = needs_to_buy_card_in_level(1)
        if card:
            return card
        return None

    def make_turn(self, board: Board) -> Turn:
        card = self.needs_to_buy_card(board)
        if card:
            if card in board.opened_development_cards[1] or board.opened_development_cards[2] or board.opened_development_cards[3]:
                result = Turn.BUY_BOARD_CARD
            else:
                result = Turn.BUY_HAND_CARD
            self.buy_development_card(board, card)
            return result
        
        stuck = set()
        while True:
            if len(stuck) == 3:
                return Turn.FAILED
            random_turn = random.randint(1, 3)
            if random_turn == 1:
                resources = self.needs_take_three_resources(board)
                if resources:
                    self.take_three_resources(resources, board)
                    return Turn.THREE_CARDS
                stuck.add(1)
                
            elif random_turn == 2:
                resources = self.needs_take_two_resources(board)
                if resources:
                    self.take_two_resources(resources, board)
                    return Turn.TWO_CARDS
                stuck.add(2)
            elif random_turn == 3:
                if self.needs_take_gold_and_card(board):
                    card_level = 1
                    if self.points >= 4 and self.points <= 7:
                        card_level = 2
                    if self.points > 7:
                        card_level = 3
                    found_level = False
                    while not found_level:
                        if len(board.closed_development_cards[card_level]) == 0:
                            card_level = ((card_level + 1) % 3) + 1
                        found_level = True
                    self.take_gold_and_card(board, card_level)
                    return Turn.GOLD_AND_CARD
                stuck.add(3)
