import pytest
from app import addition, subtraction,multiplication
def test_addition():
    assert addition(3,2) == 5
def test_subtraction():
    assert subtraction(3,2) == 1
def test_multiplication():
    assert multiplication(3,2) == 6
