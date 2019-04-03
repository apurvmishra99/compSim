import numpy as np
import matplotlib.pyplot as plt


class Traffic(object):
    def __init__(self, roadDensity=0.5, nIter=10):
                # initialize the class variables
        self.roadL = 10
        self.roadDensity = roadDensity
        # assigning to posCar the exact distribution of 0s and 1s, i.e. cars and free spaces
        self.posCar = np.array([0]*int((1-self.roadDensity) *
                                       self.roadL) + [1]*int(self.roadL*self.roadDensity))
        self.posCarEveryIter = np.zeros((nIter, self.roadL), dtype=int)
        self.nIter = nIter
        self.avgSpeeds = []
        self.steadyAvgSpeed = 0

    def mode1(self, arr):
        values, counts = np.unique(arr, return_counts=True)
        m = counts.argmax()
        return values[m]

    def update(self):
                # updation function for the movement of cars
        seed1 = np.random.randint(100000)
        np.random.seed(seed1)
        # shuffling the order of cars in posCar so we have a random distribution of cars and free space
        np.random.shuffle(self.posCar)

        print(self.posCar.shape)
        self.posCarEveryIter[0] = self.posCar
        # iterating for the user inputted amount
        for i in range(1, self.nIter):
            n = 0
            movCars = 0
            root = np.copy(self.posCarEveryIter[i-1])
            # the updation rules for movement of cars
            while n < self.posCar.size - 1:
                front = (n+1) % self.posCar.size
                back = (n-1) % self.posCar.size
                if self.posCarEveryIter[i-1][n] == 1 and self.posCarEveryIter[i-1][front] == 0:
                    root[n] = 0
                    root[front] = 1
                    movCars += 1

                elif self.posCarEveryIter[i-1][n] == 0 and self.posCarEveryIter[i-1][back] == 1:
                    root[n] = 1
                    root[back] = 0
                    movCars += 1
                n += 1
            try:
                self.avgSpeeds.append(movCars/int(self.roadDensity * self.roadL))
            except ZeroDivisionError as zde:
                self.avgSpeeds.append(0.0)
            # appending the state of road to the 2d array which stores the state of roads
            self.posCarEveryIter[i] = root
            self.steadyAvgSpeed = self.avgSpeeds[-1]

    def plotMovement(self):
        # plotting movement of cars through imshow
        plt.ylabel("No. of iterations")
        plt.xlabel("Road")
        plt.imshow(self.posCarEveryIter, interpolation=None, origin='lower', cmap='hot')
        plt.show()
