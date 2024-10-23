import pytest
import main as mn
import numpy.ma.testutils import assert_almost_equal

def test_hello_world():
    assert mn.hello_world() is True

def test_gorditas():
    assert mn.gorditas() is True

def test_get_min():
    resultado1 =mn.get_min([1,2,3])
    assert resultado1 == 1

#def test_get_min2():
#   resultado2 =mn.get_min([3,0,-1,8,6])
#    assert_almost_equal(resultado2, -9, 1)

def test_get_max1():
    resultado1 =mn.get_max([3,0,-1,8,6])
    assert resultado1 == 8

def test_get_max2():
    resultado2 =mn.get_max([6,0,12,8,1])
    assert resultado2 == 12