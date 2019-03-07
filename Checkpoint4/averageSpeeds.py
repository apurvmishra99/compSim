import numpy as np
import matplotlib.pyplot as plt
from Traffic import Traffic

def main():
	iteration = int(input("Enter the no. of iterations: "))
	car_density = 0.0
	avg_speeds = np.zeros((1,11))

	while i < 11:
		traffic = Traffic(car_density, iteration)
		traffic.update()
		avg_speeds[i] = traffic.steadyAvgSpeed
		car_density += 0.1
		i += 1

	plt.title("Avg Speed VS Car Density")
	plt.plot(avg_speeds)
	plt.xlabel("Car Density")
	plt.ylabel("Avg Speeds")
	plt.show()

if __name__ == "__main__":
	main()
