from Traffic import Traffic
from scipy.stats import mode

def main():
    x, y = [float(val) for val in input(
        "Enter the density of cars on the road and the number of iterations you want: ").split(" ")]
    test = Traffic(x,int(y))
    test.update()
    test.plotMovement()
    test.plotSpeeds()
    print(test.avgSpeeds)
    print(mode(test.avgSpeeds))
if __name__ == "__main__":
    main()
