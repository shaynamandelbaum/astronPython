import constants


class Movement:
    def __init__(self, exist: bool, direction: constants.Direction, num: int):
        self.exist = exist
        self.direction = direction
        self.num = num


class PlayerCards:
    def __init__(self, plane_movement: Movement, board_movement: Movement):
        self.plane_movement = plane_movement
        self.board_movement = board_movement


class HazardCards:
    def __init__(self, point_value: int):
        if not (point_value in constants.HAZARD_NUMBERS):
            raise ValueError("not valid airport landing card value")
        else:
            self.point_value = point_value


class AirportLandingCards:
    def __init__(self, point_value: int):
        if not (point_value in constants.AIRPORT_LANDING_NUMBERS):
            raise ValueError("not valid airport landing card value")
        else:
            self.point_value = point_value
