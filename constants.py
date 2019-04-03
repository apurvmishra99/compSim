import scipy.constants as const
class constants(object):
    GRAVITATIONAL_CONSTANT = const.gravitational_constant
    DISTANCE_EPS = 1e-16


    def reset_to_defaults(self):
        global GRAVITATIONAL_CONSTANT, DISTANCE_EPS
        GRAVITATIONAL_CONSTANT = const.gravitational_constant
        DISTANCE_EPS = 1e-16
