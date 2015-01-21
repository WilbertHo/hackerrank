#!/usr/bin/env python

from nose.tools import eq_

from utopiantree import calc_height

def test_calc_height():
    eq_(calc_height(0), 1)
    eq_(calc_height(1), 2)
    eq_(calc_height(2), 3)
    eq_(calc_height(3), 6)
    eq_(calc_height(4), 7)
