from collections import Counter


NobleTileScore = 3

class NobleTile:
    def __init__(self, cost: Counter) -> None:
        self.score: int = NobleTileScore
        self.cost: Counter = cost
