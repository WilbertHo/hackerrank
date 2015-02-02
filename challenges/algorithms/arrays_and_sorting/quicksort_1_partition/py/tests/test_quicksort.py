from nose.tools import eq_
import quicksort

def test_quicksort():
    eq_(quicksort.partition([4, 5, 3, 7, 2]), [3, 2, 4, 5, 7])
