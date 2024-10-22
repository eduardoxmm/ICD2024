import pytest
import main as mn

def test_hello_world():
    assert mn.hello_world() is True

def test_get_min():
    resultado1 =mn.get_min([1,2,3])
    assert resultado1 is 1

def test_get_min2():
    resultado2 =mn.get_min([3,0,-1,8,6])
    assert resultado2 is -1