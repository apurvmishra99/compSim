from mandelbrot import Mandelbrot


def main():
    # creating the object for the mandelbrot class with needed information
    mandel = Mandelbrot(-2.025, 0.6, -1.125, 1.125, 1024, 1024, 255)
    # calling the plot method for the object
    mandel.plot_mandelbrot()


if __name__ == "__main__":
    main()
