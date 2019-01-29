import math
import numpy as np


class Atom(object):

	def __init__(self, N=50, decayConst=0.02775, timeStep=0.01):
		# Initialising the object with values provided by the user,
		# defaulting to standard Iodine-128 values if not provided.
		self.nuclei = np.ones((N, N), dtype=int)
		self.decayConst = decayConst
		self.timeStep = timeStep
		self.decayedNumber = 0
		self.p = self.decayConst * self.timeStep

	def simHalfLife(self):
		# simulating half-life using monte carlo simulation
		# the nuclius is deacyed if the random probability is smaller than given probability
		# terminated at the point where no. of decayed nuclei become half of the total nuclei using a for - else loop
		counter = 0
		while self.decayedNumber < self.nuclei.size/2:

			for i in range(0, self.nuclei.shape[0]):
				for j in range(0, self.nuclei.shape[1]):
					if self.p >= np.random.uniform(0.0, 1.0) and self.nuclei[i][j] == 1.0:
						self.nuclei[i][j] = 0
						self.decayedNumber += 1
						if self.decayedNumber >= self.nuclei.size:
							break
				else:
					continue
				break

			counter += 1
		return float(counter*self.timeStep)

	def showAtom(self):
		# Printing the simulated decay of radioactive atom using monte carlo simulation
		print('\n'.join([' '.join([str(cell)
								   for cell in row]) for row in self.nuclei]))

	def undecayedAtoms(self):

		# returns the no. of undecayed nuclei (always half of the total number)

		return self.nuclei.size - self.decayedNumber

	def actualHalfLife(self):

		# returns the half life calculated using the mathematical formula

		return math.log(2) / self.decayConst
