"""
test for measure module
"""

import molecool
import numpy as np

def test_calculate_distance():
    r1=np.array([0,0,0])
    r2=np.array([0,1,0])

    expected_dist= 1

    calculate_distance = molecool.calculate_distance(r1,r2)

    assert (calculate_distance==expected_dist)


