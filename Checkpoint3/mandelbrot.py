import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot(object):
    def __init__(self, xmin, xmax, ymin, ymax, width, height, maxiter):
        
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.maxiter = maxiter
        self.mandelbrot_atlas = np.empty((self.width,self.height))

    def mandelbrot_function(self,complex_number):

        z = complex(0,0)
        for num_iterations in range(self.maxiter):
            if abs(z) > 2:
                return num_iterations
            z = z*z + complex_number
        return 0
    
    def mandelbrot_points(self):
        real = np.linspace(self.xmin, self.xmax, self.width)
        imaginary = np.linspace(self.ymin, self.ymax, self.height)
        
        for i in range(self.width):
            for j in range(self.height):
                self.mandelbrot_atlas[i,j] = self.mandelbrot_function(complex(real[i],imaginary[j]))

    def plot_mandelbrot(self):
        self.mandelbrot_points()
        plt.imshow(self.mandelbrot_atlas.T)
        plt.show()
