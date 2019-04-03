from itertools import combinations
import scipy.constants as const



class SolarSystem:
    def __init__(self, bodies=None):
        self.bodies = bodies or []
        self.accelerations = [
            b.force(self.bodies) / b.mass
            for b in self.bodies
        ]
        self.old_acc = [
            b.force(self.bodies) / b.mass
            for b in self.bodies
        ]

    @property
    def total_energy(self):
        return self.potential_energy + self.kinetic_energy

    @property
    def potential_energy(self):
        return -0.5*const.gravitational_constant * sum(
            b1.mass * b2.mass / b1.distance(b2)
            for b1, b2 in combinations(self.bodies, 2)
        )

    @property
    def kinetic_energy(self):
        return sum(b.kinetic_energy for b in self.bodies)

    def __len__(self):
        return len(self.bodies)

    def do_beeman(self, delta_t):
        k = 0
        for i, (a, body) in enumerate(zip(self.accelerations, self.bodies)):
            body.position += (body.velocity * delta_t) + ((1/6)*(4*a - self.old_acc[k] ))* (delta_t*delta_t)
            k+=1
        
        k=0
        for i, (a, body) in enumerate(zip(self.accelerations, self.bodies)):
            new_a = body.force(self.bodies) / body.mass
            body.velocity += ((1.0/6.0) * ((2*new_a)+(5*a)-self.old_acc[k]) * delta_t)
            self.old_acc[k] = self.accelerations[i]
            self.accelerations[i] = new_a
            k+=1
