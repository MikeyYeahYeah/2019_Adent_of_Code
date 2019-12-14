import sys
sys.path.append('..')
import lib.fuel as fuel

def test_calculator():
    assert fuel.calculator(12) == 2
    assert fuel.calculator(14) == 2
    assert fuel.calculator(1969) == 654
    assert fuel.calculator(100756) == 33583
