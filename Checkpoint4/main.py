from Traffic import Traffic
import numpy as np

def main():
    # getting the input from the user
    x, y = [float(val) for val in input(
        "Enter the density of cars on the road and the number of iterations you want: ").split(" ")]
    test = Traffic(x, int(y))  # creating object of the class
    test.update()  # applying the updation rules
    test.plotMovement()

if __name__ == "__main__":
    main()
