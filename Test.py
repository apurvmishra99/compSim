from Simulate import Simulation
import matplotlib.pyplot as plt
import numpy as np

# Testing the simulation


def main():
    sim = Simulation()
    sim.run()
    print(sim.period/sim.period[3])
    print(sim.satalite_meeting/sim.period[3])
    plot = np.array(sim.toteng)
    plt.plot(plot)
    plt.xlabel('Time')
    plt.ylabel('Total Energy')
    plt.show()


main()