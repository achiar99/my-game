from __future__ import annotations
import random
from typing import Counter, Dict, List
from .noble_tile import NobleTile
from .development_card import DevelopmentCard
from .resource import Resources
from typing import TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from board import Board


class Turn(Enum):
    FAILED = 1
    THREE_CARDS = 2
    TWO_CARDS = 3
    GOLD_AND_CARD = 4
    BUY_HAND_CARD = 5
    BUY_BOARD_CARD = 6


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.development_cards_in_hand: List[DevelopmentCard] = []
        self.development_cards: List[DevelopmentCard] = []
        self.resources: Counter = Counter({Resources.GOLD: 0, Resources.DIAMOND: 0, Resources.EMERALD: 0,
                                           Resources.ONYX: 0, Resources.RUBY: 0, Resources.SAPPHIRE: 0})
        self.noble_tiles: List[NobleTile] = []

    @property
    def points(self) -> int:
        points = 0
        for development_card in self.development_cards:
            points += development_card.score
        for noble_tile in self.noble_tiles:
            points += noble_tile.score
        return points

    def take_noble_tiles(self, borad: Board) -> None:
        discount = self.get_discount()
        noble_tiles_to_take = []
        for noble_tile in borad.noble_tiles:
            if noble_tile.score[Resources.DIAMOND] <= discount[Resources.DIAMOND] and \
               noble_tile.score[Resources.EMERALD] <= discount[Resources.EMERALD] and \
               noble_tile.score[Resources.ONYX] <= discount[Resources.ONYX] and \
               noble_tile.score[Resources.RUBY] <= discount[Resources.RUBY] and \
               noble_tile.score[Resources.SAPPHIRE] <= discount[Resources.SAPPHIRE]:
                noble_tiles_to_take.append(noble_tile)
        
        for noble_tile in noble_tiles_to_take:
            borad.noble_tiles.remove(noble_tile)
            self.noble_tiles.append(noble_tile)

    def get_total_resource_count(self) -> int:
        current_count = 0
        for _, count in self.resources.items():
            current_count += count
        return current_count

    def get_discount(self) -> Dict[Resources, int]:
        discount: Dict[Resources, int] = { Resources.DIAMOND: 0,Resources.EMERALD: 0,
                                           Resources.ONYX: 0, Resources.RUBY: 0, Resources.SAPPHIRE: 0}
        for card in self.development_cards:
            discount[card.gift] += 1
        return discount

    def buy_development_card(self, board: Board, development_card: DevelopmentCard) -> Turn:
        discount = self.get_discount()
        missing = 0
        for resource, amount in development_card.cost.items():
            available = self.resources[resource] + discount.get(resource, 0)
            current_missing =  amount - available
            if available < amount:
                missing += current_missing
            if discount.get(resource, 0) >= amount:
                continue
            if current_missing < 0:
                current_missing = 0
            resource_actual_pay = amount - discount.get(resource, 0) - max(current_missing, 0)
            self.resources[resource] -= resource_actual_pay
            board.resources[resource] += resource_actual_pay
            if self.resources[resource] < 0:
                raise Exception('Minus is not allowed')
        self.resources[Resources.GOLD] -= missing
        board.resources[Resources.GOLD] += missing
        self.development_cards.append(development_card)
        if development_card in board.opened_development_cards[development_card.level]:
            board.opened_development_cards[development_card.level].remove(development_card)
            level = development_card.level
            if board.closed_development_cards[level]:
                board.opened_development_cards[level].append(board.closed_development_cards[level][0])
                board.closed_development_cards[level] = board.closed_development_cards[level][1:]
        if development_card in self.development_cards_in_hand:
            self.development_cards_in_hand.remove(development_card)

    def take_three_resources(self, resources_to_take: List[Resources], board: Board) -> None:
        current_count = self.get_total_resource_count()
        maximum_to_take = min(10 - current_count, 3)
        removed = 0
        resources = [Resources.DIAMOND, Resources.EMERALD, Resources.ONYX, Resources.RUBY, Resources.SAPPHIRE]
            
        if maximum_to_take < len(resources_to_take):
            while (removed < len(resources_to_take)):
                random_resource = random.choice(resources)
                if self.resources[random_resource] > 0:
                    self.resources[random_resource] -= 1
                    board.resources[random_resource] += 1
                    removed += 1

        for resource in resources_to_take:
            self.resources[resource] += 1
            board.resources[resource] -= 1

    def take_two_resources(self, resource: Resources, board: Board) -> None:
        current_count = self.get_total_resource_count()
        maximum_to_take = min(10 - current_count, 3)
        removed = 0
        resources = [Resources.DIAMOND, Resources.EMERALD, Resources.ONYX, Resources.RUBY, Resources.SAPPHIRE]
        if maximum_to_take < 2:
            while (removed < 2):
                random_resource = random.choice(resources)
                if self.resources[random_resource] > 0:
                    self.resources[random_resource] -= 1
                    board.resources[random_resource] += 1
                    removed += 1
        self.resources[resource] += 2
        board.resources[resource] -= 2

    def take_gold_and_card(self, board: Board, card_level: int = 0, card: DevelopmentCard = None) -> None:
        if card:
            self.development_cards_in_hand.append(card)
            if len(board.closed_development_cards[card.level]) > 0:
                new_card = board.closed_development_cards[card_level][0]
                board.closed_development_cards[card.level] = board.closed_development_cards[card.level][1:]
                board.opened_development_cards[card.level].remove(card)
                board.opened_development_cards[card.level].append(new_card)
                
        elif card_level:
            if len(board.closed_development_cards[card_level]) > 0:
                card = board.closed_development_cards[card_level][0]
                board.closed_development_cards[card_level] = board.closed_development_cards[card_level][1:]
                self.development_cards_in_hand.append(card)

        if board.resources[Resources.GOLD] == 0:
            return

        current_count = self.get_total_resource_count()
        maximum_to_take = min(10 - current_count, 1)
        removed = 0
        resources = [Resources.DIAMOND, Resources.EMERALD, Resources.ONYX, Resources.RUBY, Resources.SAPPHIRE]
        if maximum_to_take == 0:
            while (removed < 1):
                random_resource = random.choice(resources)
                if self.resources[random_resource] > 0:
                    self.resources[random_resource] -= 1
                    board.resources[random_resource] += 1
                    removed += 1

        self.resources[Resources.GOLD] += 1
        board.resources[Resources.GOLD] -= 1
