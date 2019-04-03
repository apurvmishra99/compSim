import numpy as np
from scipy.spatial.distance import euclidean

from core import gravitational_force


class Body:

    def __init__(self, position, velocity, mass):
        self._position = np.asanyarray(position, dtype='float64')
        self._velocity = np.asanyarray(velocity, dtype='float64')
        self.mass = mass
        self.oldacc = []
        self.system = None
        self.ori = self.original()

    def original(self):
        pos = [self.position[0],self.position[1]]
        abc = np.asanyarray(pos, dtype='float64')
        return abc

    def distance(self, other):
        return euclidean(self.position, other.position)

    def force(self, other):
        '''The gravitational force other inflicts on this Body
        other can either be a Body or an iterable of Body
        '''
        if isinstance(other, self.__class__):
            return gravitational_force(
                self.mass, other.mass,
                self.position,  other.position,
            )
        else:
            force = np.zeros_like(self.position)
            for body in other:
                force += gravitational_force(
                    self.mass, body.mass,
                    self.position,  body.position,
                )
            return force

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * np.linalg.norm(self.velocity)**2

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = np.asanyarray(value, dtype='float64')

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = np.asanyarray(value, dtype='float64')
