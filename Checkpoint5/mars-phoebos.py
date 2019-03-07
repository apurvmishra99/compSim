from vpython import *
import numpy as np

#Earth-Moon gravity Emmulation

#IMPORTANT CONSTANTS

G = 6.67e-11  # Newton's Constant

MM = 6.4185e23  # Mars's Mass
PM = 1.06e16  # Phobos's Mass

ER = 3.39e6  # Mars's Radius
MR = 1.1e4  # Phobos's Radius

Distance = 9.3773e6


Mars = sphere(pos=vector(0, 0, 0), radius=ER, color=color.red)
Mars.m = MM
Mars.v = vector(0, 0, 0)  # Velocity
Mars.p = Mars.m*Mars.v  # Momentum

Phobos = sphere(pos=vector(Distance, 0, 0), radius=MR,
              color=vector(0.5, 0.5, 0.5), make_trail=True)

Phobos.m = PM
Phobos.v = vector(0, np.sqrt(G*Mars.m/Distance), 0)
Phobos.p = Phobos.m*Phobos.v

dt = 1

while True:
	Vec = Phobos.pos - Mars.pos
	Fg = -G*Mars.m*Phobos.m/mag(Vec)**3*Vec  # Vector form of the Gravity Equation

	# 1. We will update the momentum according to Pf = FΔt + Pi

	Mars.p = -Fg*dt + Mars.p
	Phobos.p = Fg*dt+Phobos.p  # -Fg becDistancese forces are equal and opposite

	#2. Update the velocites of each object, p = mv, so v = m/p

	Mars.v = Mars.p/Mars.m
	Phobos.v = Phobos.p/Phobos.m

	#3. Update the positions
	Mars.pos = Mars.pos + Mars.v*dt
	Phobos.pos = Phobos.pos + Phobos.v*dt
	print("Vector Velocity: ", Phobos.v, "Magnitutde: ", mag(Phobos.v))
	rate(10000)
