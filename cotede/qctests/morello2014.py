# -*- coding: utf-8 -*-

"""
    Quality Control based on anomaly detection
"""


import numpy as np
from cotede.fuzzy import fuzzyfy


def morello2014(features, cfg):
    """

    """
    f = fuzzyfy(features, cfg)

    ## This is how Timms and Morello defined the Fuzzy Logic approach
    #flag = np.zeros(N, dtype='i1')
    # Flag must be np.array, not a ma.array.
    flag = np.zeros(features[features.keys()[0]].shape, dtype='i1')

    flag[(f['low'] > 0.5) & (f['high'] < 0.3)] = 2
    flag[(f['low'] > 0.9)] = 1
    # Everything else is flagged 3
    flag[(f['low'] <= 0.5) | (f['high'] >= 0.3)] = 3
    # Missing check if threshold was crossed, to flag as 4
    # The thresholds coincide with the end of the ramp for the fuzzy set high,
    #   hence we can simply
    flag[(f['high'] == 1.)] = 4

    return flag