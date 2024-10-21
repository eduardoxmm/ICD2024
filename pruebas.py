import pytest
import main as mn

def test_hello_world():
    assert mn.hello_world() is True

def test_get_mininum():
    assert mn.get_min([1,2,3]) is True