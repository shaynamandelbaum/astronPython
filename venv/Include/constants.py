# model related
from enum import Enum

HAZARD_NUMBERS = [5, 10]
AIRPORT_LANDING_NUMBERS = [10, 15]


class Direction(Enum):
    BACK = 1
    FORWARD = 2
    SIDEWAYS = 3
    DIAGONAL = 4


class Plane_Colors(Enum):
    BLACK = 1
    SILVER = 2
    RED = 3
    BLUE = 4
    YELLOW = 5
    GREEN = 6
