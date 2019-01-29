from polynomials import Polynomials


def main():
    p_1 = Polynomials([2, 0, 4, -1, 0, 6]) # creates the polynomial object with the given coefficient values
    p_2 = Polynomials([-1, -3, 0, 4.5])

    p_order1 = p_1.order() # checks order
    p_order2 = p_2.order()

    p_sum = p_1.add(p_2) # adds the 2 polynomials

    p_der = p_1.derivative() # finds the derivative of the first polynomial

    p_ader = p_der.antiDerivative(2) # finds the anti derivative of polynomial and gives the constant of integration

    print(
        f"The orders of {p_1.__str__()} and {p_2.__str__()} are : {p_order1} and {p_order2}.")
    print(
        f"The sum of {p_1.__str__()} and {p_2.__str__()} is {p_sum.__str__()}")
    print(f"The derivative of {p_1.__str__()} is {p_der.__str__()}")
    print(
        f"The anti-dervative of {p_der.__str__()} with 2 as constant of integration is {p_ader.__str__()}")


if __name__ == "__main__":
    main()
