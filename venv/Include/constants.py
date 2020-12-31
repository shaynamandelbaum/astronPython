from enum import Enum, unique


# left to do for model:
# input card data and create list
# organize better
# controller? nah, need to work on model file getting the set up data and the changing using cards and replenishing
# also make notes for someone to change if needed


# ACCOUNT FOR OVERLAP WITH PLANE AND HAZARD
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


# airport landing places:
@unique
class AirportData(Enum):
    GANDER = AIRPORT_1_LOC
    TRINIDAD = AIRPORT_2_LOC
    PARIS = AIRPORT_3_LOC
    HELSINKI = AIRPORT_4_LOC
    TEL_AVIV = AIRPORT_5_LOC
    OMSK = AIRPORT_6_LOC
    CALCUTTA = AIRPORT_7_LOC
    TOKYO = AIRPORT_8_LOC
    HONOLULU = AIRPORT_9_LOC
    NOME = AIRPORT_10_LOC
    SAN_FRANCISCO = AIRPORT_11_LOC


AIRPORT_LIST = [AirportData.GANDER, AirportData.TRINIDAD, AirportData.PARIS, AirportData.HELSINKI, AirportData.OMSK,
                AirportData.CALCUTTA, AirportData.TOKYO, AirportData.HONOLULU, AirportData.NOME,
                AirportData.SAN_FRANCISCO]
# make sure to note that if they are not the same, they are different!
ELECTRICAL_STORM_3_LOC = [Location(12, 6), Location(12, 7), Location(12, 8)]
MOUNTAIN_RANGE_6_LOC = [Location(16, 1), Location(16, 2), Location(16, 3), Location(17, 1), Location(17, 2),
                        Location(17, 3)]
MOUNTAINS_2_LOC = [Location(17, 6), Location(18, 6)]
HIGH_WINDS_4_LOC = [Location(18, 8), Location(18, 9), Location(18, 10), Location(19, 8)]
HIGH_PEAKS_3_LOC = [Location(22, 2), Location(23, 2), Location(23, 3)]
THUNDERSTORMS_4_LOC = [Location(24, 6), Location(24, 7), Location(24, 8), Location(24, 9)]
HIGH_PEAKS_6_LOC = [Location(28, 8), Location(29, 8), Location(29, 7), Location(30, 7), Location(31, 7),
                    Location(32, 7)]
TORNADO_8_LOC = [Location(31, 2), Location(31, 3), Location(32, 2), Location(32, 3), Location(32, 4), Location(32, 5),
                 Location(33, 5), Location(33, 6)]
MONSOON_RAINS_2_LOC = [Location(35, 8), Location(35, 9)]
BLIZZARD_3_LOC = [Location(36, 1), Location(36, 2), Location(36, 3)]
STRONG_WINDS_2_LOC = [Location(40, 5), Location(40, 6)]
STRONG_WINDS_1_LOC = [Location(41, 8)]
HEAVY_FOG_1_LOC = [Location(42, 8)]
HEAVY_RAIN_1_LOC = [Location(43, 9)]
HAIL_STORM_1_LOC = [Location(42, 3)]
PEAKS_1_LOC = [Location(43, 3), Location(44, 2), Location(47, 1), Location(48, 2), Location(49, 3)]
SLEET_STORM_1_LOC = [Location(43, 2)]
ENGINE_TROUBLE_1_LOC = [Location(44, 9), Location(46, 1)]
HIGH_WINDS_1_LOC = [Location(45, 1)]
HIGH_PEAKS_2_LOC = [Location(50, 4), Location(51, 4)]
AIR_POCKET_1_LOC = [Location(45, 10)]
DRIVING_RAIN_1_LOC = [Location(46, 10)]
FOG_1_LOC = [Location(47, 10)]
RADAR_TROUBLE_1_LOC = [Location(48, 9)]
POOR_VISIBILITY_2_LOC = [Location(49, 8), Location(50, 8)]


# hazard places:
@unique
class HazardData(Enum):
    ELECTRICAL_STORM_3 = ELECTRICAL_STORM_3_LOC
    MOUNTAIN_RANGE_6 = MOUNTAIN_RANGE_6_LOC
    MOUNTAINS_2 = MOUNTAINS_2_LOC
    HIGH_WINDS_4 = HIGH_WINDS_4_LOC
    HIGH_PEAKS_3 = HIGH_PEAKS_3_LOC
    THUNDERSTORMS_4 = THUNDERSTORMS_4_LOC
    HIGH_PEAKS_6 = HIGH_PEAKS_6_LOC
    TORNADO_8 = TORNADO_8_LOC
    MONSOON_RAINS_2 = MONSOON_RAINS_2_LOC
    BLIZZARD_3 = BLIZZARD_3_LOC
    STRONG_WINDS_2 = STRONG_WINDS_2_LOC
    STRONG_WINDS_1 = STRONG_WINDS_1_LOC
    HEAVY_FOG_1 = HEAVY_FOG_1_LOC
    HEAVY_RAIN_1 = HEAVY_RAIN_1_LOC
    HAIL_STORM_1 = HAIL_STORM_1_LOC
    PEAKS_1 = PEAKS_1_LOC
    SLEET_STORM = SLEET_STORM_1_LOC
    ENGINE_TROUBLE_1 = ENGINE_TROUBLE_1_LOC
    HIGH_WINDS_1 = HIGH_WINDS_1_LOC
    HIGH_PEAKS_2 = HIGH_PEAKS_2_LOC
    AIR_POCKET_1 = AIR_POCKET_1_LOC
    DRIVING_RAIN_1 = DRIVING_RAIN_1_LOC
    FOG_1 = FOG_1_LOC
    RADAR_TROUBLE_1 = RADAR_TROUBLE_1_LOC
    POOR_VISIBILITY_2 = POOR_VISIBILITY_2_LOC


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
