from enum import Enum


class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# variables that can be changed
HAZARD_NUMBERS = [5, 10]
AIRPORT_LANDING_NUMBERS = [10, 15]

# starting places
STARTING_PLACES_1 = Location(2, 2)
STARTING_PLACES_2 = Location(2, 4)
STARTING_PLACES_3 = Location(2, 7)
STARTING_PLACES_4 = Location(2, 9)
STARTING_PLACES_5 = Location(2, 3)
STARTING_PLACES_6 = Location(2, 8)


# airport landing places:
class AirportName(Enum):
    GANDER = 1
    TRINIDAD = 2
    PARIS = 3
    HELSINKI = 4
    TEL_AVIV = 5
    OMSK = 6
    CALCUTTA = 7
    TOKYO = 8
    HONOLULU = 9
    NOME = 10
    SAN_FRANCISCO = 11


AIRPORT_1_LOC = [Location(8, 2), Location(8, 3), Location(8, 4)]
AIRPORT_2_LOC = [Location(8, 7), Location(8, 8), Location(8, 9)]
AIRPORT_3_LOC = [Location(15, 6), Location(15, 7)]
AIRPORT_4_LOC = [Location(18, 1), Location(18, 2)]
AIRPORT_5_LOC = [Location(21, 8), Location(21, 9)]
AIRPORT_6_LOC = [Location(26, 3), Location(26, 4)]
AIRPORT_7_LOC = [Location(32, 8), Location(32, 9)]
AIRPORT_8_LOC = [Location(39, 5), Location(39, 6)]
AIRPORT_9_LOC = [Location(45, 8), Location(45, 9)]
AIRPORT_10_LOC = [Location(47, 4), Location(47, 5)]
AIRPORT_11_LOC = [Location(51, 6), Location(51, 7)]


class Airport:
    def __init__(self, locs: list, name: AirportName):
        self.locs = locs
        self.name = name


AIRPORT_LIST = [Airport(AIRPORT_1_LOC, AirportName.GANDER), Airport(AIRPORT_2_LOC, AirportName.TRINIDAD),
                Airport(AIRPORT_3_LOC, AirportName.PARIS), Airport(AIRPORT_4_LOC, AirportName.HELSINKI),
                Airport(AIRPORT_5_LOC, AirportName.TEL_AVIV), Airport(AIRPORT_6_LOC, AirportName.OMSK),
                Airport(AIRPORT_7_LOC, AirportName.CALCUTTA), Airport(AIRPORT_8_LOC, AirportName.TOKYO),
                Airport(AIRPORT_9_LOC, AirportName.HONOLULU), Airport(AIRPORT_10_LOC, AirportName.NOME),
                Airport(AIRPORT_11_LOC, AirportName.SAN_FRANCISCO)]


# model related
class Direction(Enum):
    BACK = 1
    FORWARD = 2
    SIDEWAYS = 3
    DIAGONAL = 4


class PlaneColors(Enum):
    BLACK = 1
    SILVER = 2
    RED = 3
    BLUE = 4
    YELLOW = 5
    GREEN = 6
    NONE = 7


class TileType(Enum):
    REGULAR = 1
    AIRPORT = 2
    HAZARD = 3
    STARTING = 4
