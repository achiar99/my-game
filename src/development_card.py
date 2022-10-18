from collections import Counter
from .resource import Resources

class DevelopmentCard:
    def __init__(self, score: int, gift: Resources, cost: Counter, level: int) -> None:
        self.score: int = score
        self.gift: Resources = gift
        self.cost: Counter = cost
        self.level: int = level
