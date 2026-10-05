import pytest
from app import addition, subtraction,multiplication
def test_addition(a = 3,b = 2):
    assert addition(a, b) == 5
def test_subtraction(a = 3,b = 2):
    assert subtraction(a,b) == 1
def test_multiplication(a = 3,b = 2):
    assert multiplication(a , b) == 6
