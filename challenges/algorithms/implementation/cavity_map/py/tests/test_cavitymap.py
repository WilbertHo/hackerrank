from nose.tools import eq_
from cavitymap import map_cavities


def test_cavitymap():
    eq_(map_cavities(['1112', '1912', '1892', '1234']), ['1112', '1X12', '18X2', '1234'])
