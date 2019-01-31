import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot(object):
    # initialising the class with all the data needed to plot the mandelbrot set, width and height set the dimension of the image
    def __init__(self, xmin, xmax, ymin, ymax, width, height, maxiter):

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.maxiter = maxiter
        self.mandelbrot_atlas = np.empty((self.width, self.height))

    def mandelbrot_function(self, complex_number):
        # The function to calculate the no. of iterations it takes for z to deviate
        z = complex(0, 0)
        for num_iterations in range(self.maxiter):
            if abs(z) > 2:
                return num_iterations
            z = z*z + complex_number
        return 0

    def mandelbrot_points(self):
        # assign points to the mandelbrot atlas for plotting
        real = np.linspace(self.xmin, self.xmax, self.width)
        imaginary = np.linspace(self.ymin, self.ymax, self.height)

        for i in range(self.width):
            for j in range(self.height):
                # calling mandelbrot function
                self.mandelbrot_atlas[i, j] = self.mandelbrot_function(
                    complex(real[i], imaginary[j]))

    def plot_mandelbrot(self):
        # Plotting the madelbrot set with matplotlib

        # Calling the mandelbrot_points method to give values to the atlas
        self.mandelbrot_points()
        plt.rcParams.update({'font.size': 50})
        plt.imshow(self.mandelbrot_atlas.T, interpolation="nearest",
                   extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        plt.ylabel("Imaginary Axis")
        plt.xlabel("Real Axis")
        plt.title("Mandelbrot Set")
        plt.gray()
        plt.savefig("mandelbrot.png")
        plt.show()
