from nose.tools import eq_
from insertionsort import insertion_sort

def test_insertion_sort():
    insort = insertion_sort([1, 4, 3, 5, 6, 2])

    eq_(next(insort), [1, 4, 3, 5, 6, 2])
    eq_(next(insort), [1, 3, 4, 5, 6, 2])
    eq_(next(insort), [1, 3, 4, 5, 6, 2])
    eq_(next(insort), [1, 3, 4, 5, 6, 2])
    eq_(next(insort), [1, 2, 3, 4, 5, 6])
