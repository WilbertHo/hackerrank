from nose.tests import eq_
from cavitymap import CavityMap


def test_cavitymap():
    eq_(CavityMap.map_cavities(['1112', '1912', '1892', '1234']), ['1112', '1X12', '18X2', '1234'])
