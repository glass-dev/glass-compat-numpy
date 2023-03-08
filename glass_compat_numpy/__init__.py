'''Compatibility layer for Numpy.'''

import sys


def random_namespace(*objs):
    if 'numpy' not in sys.modules:
        raise TypeError
    import numpy as np
    for obj in objs:
        if not isinstance(obj, (np.ndarray, np.generic, np.random.Generator)):
            raise TypeError
    from . import random
    return random


def healpix_namespace(*objs):
    if 'numpy' not in sys.modules:
        raise TypeError
    import numpy as np
    for obj in objs:
        if not isinstance(obj, (np.ndarray, np.generic)):
            raise TypeError
    from . import healpix
    return healpix
