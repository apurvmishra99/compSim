import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from body import Body
from system import SolarSystem


class Simulation:
    # Making the simulation object
    def __init__(self):
        data = np.genfromtxt("test_data.csv", delimiter=',', skip_header=1, usecols=(1, 2, 3, 4, 5))
        bodies = []
        for body in range(0, data[:, 0].size):
            pos = np.array([data[body][1], data[body][2]])
            mass = np.array([data[body][0]])
            velocity = np.array([data[body][3], data[body][4]])
            b1 = Body(pos,velocity,mass)
            bodies.append(b1)
        self.colours = ['Yellow', 'gray', 'magenta', 'blue','red','white']
        n_years = 3
        n_steps = 100000
        delta_t = n_years * np.pi * 1e7 / n_steps
        #2*np.pi*(143e2)
        self.dt = 525600
        self.sys = SolarSystem(bodies)
        self.patches = []
        self.iter = 30000
        self.toteng = []
        self.cross = []
        self.satalite_meeting = 0
        peri = []
        for i in range (0,len(bodies)):
            self.cross.append(0)
        for i in range(0,len(bodies)):
            peri.append(0)
        self.period = np.array(peri)

    def init(self):
        return self.patches
    # Running the simulation

    def run(self):
        fig = plt.figure()
        self.ax = plt.axes()
        for i , body in enumerate(self.sys.bodies):
            self.patches.append(patches.Circle((body.position), 5e9, animated=False, color=self.colours[i]))
        for i in range(0, len(self.patches)):
            self.ax.add_patch(self.patches[i])
        self.ax.axis('scaled')
        self.ax.set_xlim(-35e10, 35e10)
        self.ax.set_ylim(-35e10, 35e10)
        self.ax.patch.set_facecolor((0., 0., 0.))
        self.t = 0
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.iter, repeat=False, interval=20, blit=False)
        plt.show()
    # Animating it

    def animate(self, i):
        y_list = []
        for x in range (0,len(self.sys.bodies)):
            y = (self.sys.bodies[x]. position[1])
            y_list.append(y)
        self.sys.do_beeman(self.dt)
        y1_list = []
        for x in range (0,len(self.sys.bodies)):
            y1 = (self.sys.bodies[x]. position[1])
            y1_list.append(y1)
        mars = self.sys.bodies[4]
        sat = self.sys.bodies[5]
       # print(abs(mars.distance(sat)))
        if(abs(mars.distance(sat)) <1e10):
            self.satalite_meeting = i

        for x  in range(0,len(self.sys.bodies)):
            if(y_list[x]<=0 and y1_list[x]>=0 and self.cross[x]<=1 ):
                self.cross[x]+=1
                self.period[x] = i
        tot = self.sys.total_energy
        self.toteng.append(tot)
        for x in range(0, len(self.patches)):
            self.patches[x].center = self.sys.bodies[x].position
        return self.patches
