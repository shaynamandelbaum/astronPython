import constants
import cards
class Player:
    def __init__(self, plane_color: constants.Plane_Colors, turn: bool, player_cards: cards.PlayerCards[],
                 airport_landing_cards: cards.AirportLandingCards[], hazard_cards: cards.HazardCards[]):