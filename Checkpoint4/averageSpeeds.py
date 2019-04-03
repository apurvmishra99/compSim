import numpy as np
import matplotlib.pyplot as plt
from Traffic import Traffic


def main():
    iteration = int(input("Enter the no. of iterations: "))
    car_density = 0.0
    avg_speeds = np.zeros((10,))

    for i in range(0,9):
        t = Traffic(car_density, iteration)
        t.update()
        avg_speeds[i] = t.steadyAvgSpeed
        car_density += 0.1
    print(avg_speeds)
    plt.xticks(np.arange(10), ('0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'))
    plt.title("Avg Speed VS Car Density")
    plt.plot(avg_speeds)
    plt.xlabel("Car Density")
    plt.ylabel("Avg Speeds")
    plt.show()


if __name__ == "__main__":
    main()
