import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import scipy.constants as const

GRAVITATIONAL_CONSTANT = const.gravitational_constant


class CelestialBody(object):
    def __init__(self, name="", r=(0,0), v=0, mass=1):
        self._position = np.asanyarray(r, dtype='float64')
        self._velocity = np.asanyarray(v, dtype='float64')
        self.mass = mass
        self.name = name

    def distance(self, other):
        return euclidean(self.position, other.position)

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2

    @position.setter
    def position(self, value):
        self._position = np.asanyarray(value, dtype='float64')

    @velocity.setter
    def velocity(self, value):
        self._velocity = np.asanyarray(value, dtype='float64')
   
    @staticmethod
    def gravitational_force(m1, m2, pos1, pos2):
        return -(const.GRAVITATIONAL_CONSTANT * m1 * m2 * (pos1 - pos2)) / (euclidean(pos1, pos2)**3)

    def force(self, other):
        return gravitational_force(self.mass, other.mass, self.position, other.position)
