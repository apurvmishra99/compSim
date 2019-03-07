from celestial_body import GRAVITATIONAL_CONSTANT
from celestial_body import CelestialBody
import matplotlib.pyplot as plt
import numpy as np

class EulerIntegrator:
    def __init__(self, time_step, bodies):
        self.time_step = time_step
        self.bodies = bodies

    def calculate_single_body_acceleration(self, body_index):
        acceleration = np.zeros((2,))
        target_body = self.bodies[body_index]
        for index, external_body in enumerate(self.bodies):
            if index != body_index:
                r = target_body.distance(external_body)
                tmp = GRAVITATIONAL_CONSTANT * external_body.mass / r**3
                acceleration[0] += tmp * (external_body.position[0] - target_body.position[0])
                acceleration[1] += tmp * (external_body.position[1] - target_body.position[1])
        return acceleration

    def update_location(self):
        for target_body in self.bodies:
            x_update = target_body.position[0] + target_body.velocity[0] * self.time_step
            y_update = target_body.position[1] + target_body.velocity[1] * self.time_step
            target_body.position((x_update, y_update))

    def compute_velocity(self):
        for body_index, target_body in enumerate(self.bodies):
            acceleration = self.calculate_single_body_acceleration(body_index)
            x_velocity = target_body.velocity[0] + acceleration.x * self.time_step
            y_velocity = target_body.velocity[1] + acceleration.y * self.time_step
            target_body.velocity((x_velocity, y_velocity))

    def compute_gravity_step(self):
        self.compute_velocity()
        self.update_location()

    def plot_output(self, bodies, outfile=None):
        fig = plt.figure()
        colours = ['r', 'b', 'g', 'y', 'm', 'c']
        ax = fig.add_subplot(1, 1, projection='2d')
        max_range = 0
        for current_body in bodies:
            max_dim = max(max(current_body["x"]), max(
                current_body["y"]))
            if max_dim > max_range:
                max_range = max_dim
            ax.plot(current_body["x"], current_body["y"], current_body["z"], c=random.choice(
                colours), label=current_body["name"])

        ax.set_xlim([-max_range, max_range])
        ax.set_ylim([-max_range, max_range])
        ax.legend()

    if outfile:
        plt.savefig(outfile)
    else:
        plt.show()


    def run_simulation(self, integrator, names=None, number_of_steps=10000, report_freq=100):

    #create output container for each body
        body_locations_hist = []
        for current_body in bodies:
            body_locations_hist.append(
                {"x": [], "y": [], "z": [], "name": current_body.name})

        for i in range(1, int(number_of_steps)):
            integrator.compute_gravity_step()

            if i % report_freq == 0:
                for index, body_location in enumerate(body_locations_hist):
                    body_location["x"].append(bodies[index].location.x)
                    body_location["y"].append(bodies[index].location.y)
                    body_location["z"].append(bodies[index].location.z)

        return body_locations_hist
