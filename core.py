
import scipy.constants as const
from scipy.spatial.distance import euclidean


def gravitational_force(m1, m2, pos1, pos2):
    ''' Newtons law of universal gravity in vectorial form '''
    return - (
        const.gravitational_constant
        * m1 * m2
        * (pos1 - pos2) / (euclidean(pos1, pos2) + 1e-16)**3
    )
