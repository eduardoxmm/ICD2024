import pytest
import main as mn

def test_hello_world():
    assert mn.hello_world() is True

def test_get_min():
    resultado =mn.get_min([1,2,3])
    assert resultado is 1