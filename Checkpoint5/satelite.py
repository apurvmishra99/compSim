import numpy as np
from numpy.linalg import norm

mass_sun = 1.989 * 10 ** 30
G = 6.674e-11


class Satelite(object):
    def __init__(self, origin, target, colour, size, mass, given_speed, angle,
                 radius_planet, planets):
        self.colour = colour
        self.size = size
        self.mass = mass

        # The velocity of the planet of origin plus the given velocity
        # at the given angle.
        self._velocity = np.asanyarray(origin.velocity + given_speed *
                     np.array([np.cos(angle), np.sin(angle)]), dtype='float64')

        # The position of the planet of origin plus the vector in the direction
        # of the given angle and length radius.
        tmp_pos = [origin.position[0] + radius_planet * np.cos(angle),
                   origin.position[1] + radius_planet * np.sin(angle)]
        self._position = np.asanyarray(tmp_pos, dtype='float64')
        self.acc = self.update_acc(planets)
        self.origin = origin
        self.target = target
        self.min_distance = None
        self.old_acc = self.acc

    def update_pos(self, t):
        """Obtaining the new position using the Beeman's algorithm.
        Args:
            param1 (float): a small time step.
        """
        self.position = (self.position + self.velocity * t) + \
            ((t**2 / 6.0) * (4.0 * self.acc - self.old_acc))

    def update_minimal_distance(self):
        """Updates the minimal distance to the target if the Satelite has moved
        any closer. Writes the minimal distance in a text file named
        'minimum-distance.txt.'
        """
        dist = norm(self.position-self.target.position) # Distance to the target

        if self.min_distance:  # If it's not the first iteration
            if self.min_distance > dist:
                # Update and overwrite
                self.min_distance = dist
                with open('minimum-distance.txt', 'w') as f:
                    f.write("Minimal distance to " + self.target.name +
                            ": " + str(round(self.min_distance / 1000, 2)) + " km.")

        else:
            self.min_distance = dist

    def update_vel(self, t, new_acc):
        """Obtaining the new velocity using the Beeman's algorithm.
        Args:
            param1 (float): a small time step needed for numerical integration.
            param2 (float): the acceleration at the next time step.
        """
        self.velocity = self.velocity + ((t / 6.0) *
                                ((2.0 * new_acc) + (5.0 * self.acc) - self.old_acc))

    def update_acc(self, planets):
        """Calculating the acceleration due to the planets.
        The sum of all the Gm/r, where m is the mass of the planet and r
        is the radius separating them.
        Args:
            param1 (list): a list of all the planets.
        """
        acc = np.zeros(2)
        for planet in planets:
            if planet is not self:
                dist = self.position - planet.position  # Distance between planets
                # Using Newton's gravitational formula.
                acc = acc + ((-G * planet.mass * dist) / norm(dist)**3)
        return acc

    def update_vel_acc(self, t, planets):
        """Updates the velocity and the acceleration of the satelite.
        Args:
            param1 (float): a small time step needed for numerical integration.
            param2 (list): a list of all the planets.
        """
        # First calculate the new acceleration.
        new_acc = self.update_acc(planets)
        # Calculate the velocity with it
        self.update_vel(t, new_acc)
        # Lastly, update the accelerations.
        self.old_acc, self.acc = self.acc, new_acc

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * norm(self.velocity)**2

    @position.setter
    def position(self, value):
        self._position = np.asanyarray(value, dtype='float64')

    @velocity.setter
    def velocity(self, value):
        self._velocity = np.asanyarray(value, dtype='float64')
