import numpy as np
import matplotlib.pyplot as plt


class Traffic(object):
    def __init__(self, roadDensity=0.5, nIter=10):
		#initialize the class variables
        self.roadL = 50
        self.roadDensity = roadDensity
        #assigning to posCar the exact distribution of 0s and 1s, i.e. cars and free spaces
        self.posCar = np.array([0]*int((1-self.roadDensity) *
                               self.roadL) + [1]*int(self.roadL*self.roadDensity))
        self.posCarEveryIter = np.zeros((nIter, self.roadL), dtype=int)
        self.nIter = nIter
        self.steadyAvgSpeed = 0

    @staticmethod
    def mode1(self, arr):
        values, counts = np.unique(arr, return_counts=True)
        m = counts.argmax()
        return values[m]

    def update(self):
		#updation function for the movement of cars
        seed1 = np.random.randint(100000)
        np.random.seed(seed1)
        #shuffling the order of cars in posCar so we have a random distribution of cars and free space
        np.random.shuffle(self.posCar)
        seed2 = np.random.randint(100000)
        np.random.seed(seed2)
        np.random.shuffle(self.posCar)
        self.posCarEveryIter[0] = self.posCar
        #iterating for the user inputted amount
        for i in range(1, self.nIter):
            n = 0
            movCars = 0
            root = np.copy(self.posCarEveryIter[i-1])
            avgSpeeds = []
            #the updation rules for movement of cars
            while n < self.posCar.size -1:
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

                avgSpeeds.append(movCars/int(self.roadDensity * self.roadL))
            self.posCarEveryIter[i] = root #appending the state of road to the 2d array which stores the state of roads
            self.steadyAvgSpeed = self.mode1(avgSpeeds)

    def plotMovement(self):
		#plotting movement of cars through imshow
        plt.imshow(self.posCarEveryIter, interpolation=None, origin='lower')
        plt.show()
