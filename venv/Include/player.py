import constants


class Player:
    def __init__(self, plane_color: constants.PlaneColors, turn: bool, player_cards: list,
                 airport_landing_cards: list, hazard_cards: list, loc_on_board: constants.Location):
        self.plane_color = plane_color
        self.turn = turn
        self.player_cards = player_cards
        self.airport_landing_cards = airport_landing_cards
        self.hazard_cards = hazard_cards
        self.loc_on_board = loc_on_board
