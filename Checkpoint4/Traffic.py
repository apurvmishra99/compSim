import numpy as np
import matplotlib.pyplot as plt


class Traffic(object):
    def __init__(self, roadDensity=0.5, nIter=10):
        self.roadL = 10
        self.roadDensity = roadDensity
        self.posCar = np.array([0]*int((1-self.roadDensity) *
                               self.roadL) + [1]*int(self.roadL*self.roadDensity))
        self.posCarEveryIter = np.zeros((nIter, self.roadL), dtype=int)
        self.nIter = nIter
        self.avgSpeeds = []

    def update(self):
        np.random.seed(3)
        np.random.shuffle(self.posCar)
        np.random.seed(5)
        np.random.shuffle(self.posCar)
        self.posCarEveryIter[0] = self.posCar
        for i in range(1, self.nIter):
            n = 0
            movCars = 0
            root = np.copy(self.posCarEveryIter[i-1])
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

            self.avgSpeeds.append(movCars/int(self.roadDensity * self.roadL))
            self.posCarEveryIter[i] = root

    def plotMovement(self):
        plt.imshow(self.posCarEveryIter, interpolation=None, origin='lower')
        plt.show()
    
    def plotSpeeds(self):
        plt.plot(self.avgSpeeds)
        plt.show()

