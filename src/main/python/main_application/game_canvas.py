
from PyQt5.QtWidgets import QWidget

from uct.game.base_game_move import BaseGameMove
from utils.custom_event import CustomEvent


class GameCanvas(QWidget):
    """
    Base game canvas class to be inherited from.
    """
    def __init__(self):
        super().__init__()
        self.WIDTH = 600
        self.HEIGHT = 600
        self.player_move_performed = CustomEvent()
        self.setMinimumSize(self.WIDTH, self.HEIGHT)
        self.setMaximumSize(self.WIDTH, self.HEIGHT)
        self.player_can_click = True
        self.game_ended = False

    def perform_algorithm_move(self, move: BaseGameMove):
        """
        Base class to implement the whole single move execution.
        """
        pass

    def set_player_can_click(self, value: bool):
        """
        Setter. If set false, player cannot click on canvas.

		Args:
			value:  bool

		Returns:
			None        
		"""
        self.player_can_click = value

