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

