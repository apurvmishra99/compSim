#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019 Apurv Mishra <s1864480@cplab037.ph.ed.ac.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from atom import Atom


def main():
    # Asking the user to input the values of N, decay const and time step
    N, dConst, time = input(
        " the length of the 2D,value of the decay constant λ,and the timestep Δt ").split(" ")
    # making the object of our class
    test = Atom(int(N), float(dConst), float(time))
    simHalf = test.simHalfLife()
    actualHalf = test.actualHalfLife()
    undecayedNuclei = test.undecayedAtoms()
    test.showAtom()
    print(f"The simulated half-life is {simHalf}")
    print(f"The actual half-life is {actualHalf}")
    print(f"The no. of undecayed nuclei are {undecayedNuclei}")


if __name__ == '__main__':
    main()
