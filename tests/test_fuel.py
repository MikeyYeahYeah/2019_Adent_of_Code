import sys
sys.path.append('..')
import lib.fuel as fuel

def test__calculation():
    assert fuel._calculation(12) == 2
    assert fuel._calculation(14) == 2
    assert fuel._calculation(1969) == 654
    assert fuel._calculation(100756) == 33583

def test_total():
    assert fuel.total(14) == 2
    assert fuel.total(1969) == 966
    assert fuel.total(100756) == 50346