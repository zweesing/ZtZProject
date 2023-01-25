from ..classes.pathfinder import Pathfinder
import random

class Constructive(Pathfinder):
    """ Subclass for the pathfinder class. This Algoritme determines the shortest path using depth and breth search."""
    def __init__(self, start, end, board):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        super().__init__(start, end, board)

    def find(self):
        #implementations of depth and or breth search for determining route. Implement 3D part.
