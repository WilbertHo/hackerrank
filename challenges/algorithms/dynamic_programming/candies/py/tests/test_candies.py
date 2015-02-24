from nose.tools import eq_
from candies import candies


def test_candies():
    eq_(candies([1, 2, 2]), 4)
    eq_(candies([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]), 19)
