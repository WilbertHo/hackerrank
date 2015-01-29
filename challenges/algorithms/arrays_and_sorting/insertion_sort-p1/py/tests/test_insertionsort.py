from nose.tools import eq_
from insertionsort import insertion_sort

def test_insertion_sort():
    insort = insertion_sort([2, 4, 6, 8, 3])

    eq_(next(insort), [2, 4, 6, 8, 8])
    eq_(next(insort), [2, 4, 6, 6, 8])
    eq_(next(insort), [2, 4, 4, 6, 8])
    eq_(next(insort), [2, 3, 4, 6, 8])
