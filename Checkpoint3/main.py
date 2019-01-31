from mandelbrot import Mandelbrot

def main():
    mandel = Mandelbrot(-2.025, 0.6, -1.125, 1.125, 1000, 1000, 255)
    mandel.plot_mandelbrot()


if __name__ == "__main__":
    main()