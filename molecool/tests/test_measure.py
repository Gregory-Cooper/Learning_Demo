"""
test for measure module
"""

import molecool
import numpy as np
import pytest

def test_calculate_distance():
    r1=np.array([0,0,0])
    r2=np.array([0,1,0])

    expected_dist= 1

    calculate_distance = molecool.calculate_distance(r1,r2)

    assert (calculate_distance==expected_dist)


def test_calculate_angle():
    r1=np.array([0,0,-1])
    r2=np.array([0,0,0])
    r3=np.array([1,0,0])
    expected_angle= 90
    calculate_angle1= molecool.calculate_angle(r1,r2,r3, degrees=True)

    assert (calculate_angle1==expected_angle)

@pytest.mark.parametrize("p1,p2,p3,expected_angle", [
    (np.array([np.sqrt(2)/2,np.sqrt(2)/2,0]),np.array([0,0,0]),np.array([1,0,0]),45),
    (np.array([0,0,-1]),np.array([0,1,0]),np.array([1,0,0]),60)
])
def test_calc_angle_many(p1,p2,p3,expected_angle):
    calculate_angle1= molecool.calculate_angle(p1,p2,p3, degrees=True)

    assert (pytest.approx(calculate_angle1)==expected_angle)
