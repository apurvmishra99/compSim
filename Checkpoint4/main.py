from Traffic import Traffic
import numpy as np

def mode1(x):
	values, counts = np.unique(x, return_counts=True)
	m = counts.argmax()
	return values[m]
	
def main():
	#getting the input from the user
    x, y = [float(val) for val in input(
        "Enter the density of cars on the road and the number of iterations you want: ").split(" ")]
    test = Traffic(x, int(y)) #creating object of the class
    test.update() #applying the updation rules
    test.plotMovement()
    test.plotSpeeds()
    print(mode1(test.avgSpeeds))


if __name__ == "__main__":
    main()
