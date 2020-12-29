from enum import Enum
class Direction(Enum):
    BACK = 1
    FORWARD = 2
    SIDEWAYS = 3
    DIAGONAL = 4


class Movement:
    def __init__(self, exist: bool, dir: Direction, num: int):
        self.exist = exist
        self.dir = dir
        self.num = num

class PlayerCards:
    def __init__(self, planeMovement:Movement, boardMovement:Movement):
        self.planeMovement = planeMovement
        self.boardMovement = boardMovement

class HazardCards:
    def __init__(self, pointValue: int):
        if(not(pointValue == -5 or pointValue == 10))