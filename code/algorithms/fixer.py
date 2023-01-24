# algoritme zoekt snelste pad
# randomise lengte stap of breedte stap, maar ga wel volgens snelste pad, veel if statements
#  mag niet over andere gates heen.

from ..classes.pathfinder import Pathfinder
import random


class Pathfind(Pathfinder):
    def __init__(self, start, end, board):
        super().__init__(start, end, board)

    def find(self):
        pass


# als conflict:
# check ander snelste pad, anders laat het voor nu
# zo min mogelijk conflicten over, daarna bruggetjes maken proberen
