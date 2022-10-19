from __future__ import annotations
from cmath import cos
import random
from typing import List, Optional
from ..development_card import DevelopmentCard
from ..resource import Resources
from ..player import Player, Turn
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from board import Board

class PlayerLevel1(Player):
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
        
        relevant_cards = self.development_cards_in_hand + board.opened_development_cards[1] + board.opened_development_cards[2] + board.opened_development_cards[3]
        min_missing_resources_count = 100
        min_card = None
        for relevant_card in relevant_cards:
            missing_resources_count = 0
            for resource, cost in relevant_card.cost.items():
                missing_resources_count += max(0, cost - self.resources[resource])
            if missing_resources_count < min_missing_resources_count:
                min_missing_resources_count = missing_resources_count
                min_card = relevant_card
        
        resources_to_take = []
        if min_missing_resources_count == 1:
            need_to_take = None
            for resource, cost in min_card.cost.items():
                if cost > self.resources[resource]:
                    need_to_take = resource
                    break
        
            if board.resources[need_to_take] > 0:
                resources_to_take.append(need_to_take)
            
            for resource, count in board.resources.items():
                if len(resources_to_take) == 3:
                    break
                if resource == need_to_take:
                    continue
                if count:
                    resources_to_take.append(resource)
                
            if len(resources_to_take) == 3:
                self.take_three_resources(resources_to_take, board)
                return Turn.THREE_CARDS

        if min_missing_resources_count == 2:
            need_to_take_1 = None
            need_to_take_2 = None
            for resource, cost in min_card.cost.items():
                if cost - self.resources[resource] == 1:
                    if not need_to_take_1:
                        need_to_take_1 = resource
                        continue
                    if need_to_take_1 and not need_to_take_2:
                        need_to_take_2 = resource
                        break
                if cost - self.resources[resource] == 2:
                    need_to_take_1 = resource
                    need_to_take_2 = resource
                    break
            
            if need_to_take_1 and need_to_take_2 and need_to_take_1 != need_to_take_2:
                if board.resources[need_to_take_1] > 0:
                    resources_to_take.append(need_to_take_1)
                    
                if board.resources[need_to_take_2] > 0:
                    resources_to_take.append(need_to_take_2)
            
                for resource, count in board.resources.items():
                    if len(resources_to_take) == 3:
                        break
                    if resource in [need_to_take_1, need_to_take_2]:
                        continue
                    if count:
                        resources_to_take.append(resource)
                    
                if len(resources_to_take) == 3:
                    self.take_three_resources(resources_to_take, board)
                    return Turn.THREE_CARDS
            
            if need_to_take_1 and need_to_take_2 and need_to_take_1 == need_to_take_2:
                if board.resources[need_to_take_1] >= 4 and self.get_total_resource_count() <= 8:
                    self.take_two_resources(need_to_take_1, board)
                    return Turn.TWO_CARDS

                if board.resources[need_to_take_1] > 0:
                    resources_to_take.append(need_to_take_1)
            
                for resource, count in board.resources.items():
                    if len(resources_to_take) == 3:
                        break
                    if resource == need_to_take_1:
                        continue
                    if count:
                        resources_to_take.append(resource)
                    
                if len(resources_to_take) == 3:
                    self.take_three_resources(resources_to_take, board)
                    return Turn.THREE_CARDS
        
        return self.random_turn(board)
