import pytest
from blah.hola import *


def test1():
    a = 10
    b = 20
    res1 = add_something(a, b)
    assert res1 == 30
