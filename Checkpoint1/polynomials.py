import itertools


class Polynomials(object):
    def __init__(self, coeffs=[]):
        self.coeffs = coeffs     # initialising the class and assigning the value of coefficients

    def order(self):
        # order of the polynomial is the length of coefficient list subtracted by 1
        return len(self.coeffs) - 1

    def add(self, p):
        # itertools.zip_longest zips the 2 lists while making them of the same size by filling in the given value
        # using list comprehension we sum the tuples
        return Polynomials([i+j for i, j in itertools.zip_longest(self.coeffs, p.coeffs, fillvalue=0)])

    def derivative(self):
        # this finds the derivative of the polynomial
        return Polynomials([self.coeffs[i]*i for i in range(1, len(self.coeffs))])

    def antiDerivative(self, c):
		# method takes the given constant and finds the anti derivative of the polynomial
        return Polynomials([c] + [self.coeffs[i]*(1/(i+1)) for i in range(0, len(self.coeffs))])

    def __str__(self):
		# __str__ represents the string in the required format: a0 + a1x + a2x^2 + .... + anx^n
        s = ""
        for i in range(0, len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue
            elif i == 0:
                s += str(self.coeffs[i])
            elif i == 1 and self.coeffs[i] < 0:
                s += " - " + str(-1*self.coeffs[i]) + "x"
            elif i == 1 and self.coeffs[i] > 0:
                s += " + " + str(self.coeffs[i]) + "x"
            else:
                if self.coeffs[i] > 0:
                    s += " + " + str(self.coeffs[i]) + "x^" + str(i)
                else:
                    s += " - " + str(-1 * self.coeffs[i]) + "x^" + str(i)
        return s
