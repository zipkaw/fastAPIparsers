from src.controllers.lamoda_controller import LamodaController
from src.controllers.twitch_controller import TwitchController


class ContainerController:
    def __init__(self, db, twitch, kafka):
        self._lamoda = LamodaController(db)
        self._twitch_controller = TwitchController(twitch, kafka)

    @property
    def lamoda(self):
        return self._lamoda

    @property
    def twitch(self):
        return self._twitch_controller
