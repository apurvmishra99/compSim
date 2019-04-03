import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from Celestial import Celestial

GRAVITATIONAL_CONSTANT = 6.67408e-11

class Simulation:

    def __init__(self):
        data = np.genfromtxt("test_data.csv", delimiter=',', skip_header=1, usecols=(1, 2, 3, 4, 5)) #get data from the csv file
        m = [] #mass
        p = [] #position
        v = [] #velocity
        for body in range(0, data[:, 0].size):
            m.append(np.array([data[body][0]]))
            p.append(np.array([data[body][1], data[body][2]]))
            v.append(np.array([data[body][3], data[body][4]]))
        masses = np.array(m)
        positions = np.array(p)
        velocities = np.array(v)
        v_init_phobos = (GRAVITATIONAL_CONSTANT * masses[0] / (np.linalg.norm(positions[1] - positions[0])))**0.5
        v_init_deimos = (GRAVITATIONAL_CONSTANT * masses[0] / (np.linalg.norm(positions[2] - positions[0])))**0.5
        velocities[1][1] = v_init_phobos
        velocities[2][1] = v_init_deimos
        self.colours = ['red', 'gray', 'yellow', 'blue']
        self.sys = Celestial(500, masses, positions, velocities)
        self.patches = []
        self.history = []
        self.iter = 30000
        self.time = 0.0

    def init(self):
        return self.patches

    def run(self):
        #running the animation
        fig = plt.figure()
        self.ax = plt.axes()
        for i in range(0, self.sys.scalars[0].size):
            self.patches.append(patches.Circle((self.sys.vectors[0][i]), 1.5e5, animated=False, color=self.colours[i]))
        for i in range(0, len(self.patches)):
            self.ax.add_patch(self.patches[i])
        self.ax.axis('scaled')
        self.ax.set_xlim(-25e06, 25e06)
        self.ax.set_ylim(-25e06, 25e06)
        self.ax.patch.set_facecolor((0., 0., 0.))
        self.t = 0
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.iter, repeat=False, interval=20, blit=False)
        plt.show()

    def animate(self, i): #animatio on the go
        self.sys.computeAcceleration()
        self.sys.computeVelocity()
        self.sys.computePosition()
        self.time += 8.
        if i % 250 == 0:
            self.sys.computeKE()
            print(self.sys.ke)
        if (abs(np.arctan2(self.sys.vectors[0][1][1], self.sys.vectors[0][1][0])) <= 0.001 and i > 500):
            self.t = self.time
        for x in range(0, len(self.patches)):
            self.patches[x].center = self.sys.vectors[0][x]
        return self.patches
