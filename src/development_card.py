from collections import Counter
from .resource import Resources

class DevelopmentCard:
    def __init__(self, score: int, gift: Resources, cost: Counter, level: int) -> None:
        self.score: int = score
        self.gift: Resources = gift
        self.cost: Counter = cost
        self.level: int = level

    def __str__(self) -> str:
        cost = f'red: {self.cost[Resources.RUBY]}, blue: {self.cost[Resources.SAPPHIRE]}, green: {self.cost[Resources.EMERALD]}, white: {self.cost[Resources.DIAMOND]}, black: {self.cost[Resources.ONYX]}'
        return f'level: {self.level}, gift: {self.gift}, score: {self.score}, cost: {cost}'