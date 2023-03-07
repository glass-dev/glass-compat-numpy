'''Random namespace for Numpy.'''

import numpy as np

RandomState = np.random.Generator


def random_state(seed=None):
    return np.random.default_rng(seed)


def split(rand):
    return rand, rand


def standard_normal(rand, shape=()):
    return rand, rand.standard_normal(size=shape)


def choice(rand, shape=(), replace=True, p=None, axis=0):
    return rand, rand.choice(size=shape, replace=replace, p=p, axis=axis)


def uniform(rand, low=0.0, high=1.0, shape=()):
    return rand, rand.uniform(low=low, high=high, size=shape)


def normal(rand, loc=0.0, scale=1.0, shape=()):
    return rand, rand.normal(loc=loc, scale=scale, size=shape)


def poisson(rand, lam=1.0, shape=()):
    return rand, rand.poisson(lam=lam, size=shape)
