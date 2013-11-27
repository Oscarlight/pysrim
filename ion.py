"""
A module to represent an Ion Class
"""

import math
import numpy as np
from numpy.linalg import norm

from element import Element

class Ion:
    """
    Representation of an ion
    input:
    position [x, y, z]
    direction [u, v, w] (unit vector)
    energy e (electron volts eV)
    element Element(args)
    """
    id_counter = 0
    
    def __init__(self, position, direction, energy, element):
        self.position = position
        self.direction = direction
        self.energy = energy
        self.element = element
        self.id = Ion.id_counter
        Ion.id_counter += 1

    def set_trajectory(self, trajectory):
        """
        Replaces the current position and velocity of the ion
        """
        self.position = trajectory[0]
        self.direction = trajectory[1] / norm(trajectory[1], 2)

    def moveIonByDistance(self, pathLength):
        """
        Given the current velocity direction
        displace the atom a given distance 
        """
        self.position = self.position + pathLength * self.direction
            
    def __str__(self):
        return "Position:" + str(self.position) + \
               "Direction:" + str(self.direction) + \
               "Energy: " + str(self.energy) + \
               "Element" + str(self.element)
