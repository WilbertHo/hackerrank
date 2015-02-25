from nose.tools import eq_
import maximizingxor


def test_maximizingxor():
    eq_(maximizingxor.maximize(1, 10), 15)
    eq_(maximizingxor.maximize(10, 15), 7)
