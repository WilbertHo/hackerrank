from nose.tools import eq_
import sherlockandpairs

def test_sherlockandpairs():
    eq_(sherlockandpairs.get_count([1, 2, 3]), 0)
    eq_(sherlockandpairs.get_count([1, 1, 2]), 2)
    eq_(sherlockandpairs.get_count([1, 1, 1]), 6)
    eq_(sherlockandpairs.get_count([1, 1, 1, 1]), 12)
