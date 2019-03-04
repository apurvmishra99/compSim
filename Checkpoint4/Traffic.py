import numpy as np
import matplotlib.pyplot as plt


class Traffic(object):
    def __init__(self, roadDensity, nIter):
        self.roadL = 50
        self.roadDensity = roadDensity
        self.posCar = np.array([0]*int((1-self.roadDensity) *
                               self.roadL) + [1]*int(self.roadL*self.roadDensity))
        self.posCarEveryIter = np.zeros((nIter, self.roadL), dtype=int)
        self.nIter = nIter
        self.avgSpeeds = []

    def update(self):
        np.random.shuffle(self.posCar)
        self.posCarEveryIter[0] = self.posCar
        for i in range(1, self.nIter):
            n = 0
            movCars = 0
            root = list(self.posCarEveryIter[i-1])
            while n < self.posCar.size -1:
                front = (n+1) % self.posCar.size
                back = (n-1) % self.posCar.size
                if self.posCarEveryIter[i-1][n] == 1:
                    if self.posCarEveryIter[i-1][front] == 1:
                        root[n] = 1          
                    else:
                        root[n] = 0
                        movCars += 1

                elif self.posCarEveryIter[i-1][n] == 0:
                    if self.posCarEveryIter[i-1][back] == 1:
                        root[n] = 1
                        movCars += 1
                    else:
                        root[n] = 0
                self.avgSpeeds.append(movCars/(self.roadDensity * self.roadL))
                n += 1
            self.posCarEveryIter[i] = np.array(list(root))

    def plotMovement(self):
        plt.imshow(self.posCarEveryIter, interpolation=None, origin='lower')
        plt.show()



