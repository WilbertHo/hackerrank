from nose.tools import eq_
from runningtime import insertionSort

def test_runningtime():
    eq_(insertionSort([2, 1, 3, 1, 2]), 4)
    eq_(insertionSort([1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]), 0)
    eq_(insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 45)
