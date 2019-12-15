import math

def _calculation(mass):
    """Calculates the amount of fuel required to launch"""
    return math.floor(mass / 3) - 2

def total(mass):
    """Returns the total amount fuel required"""
    fuel = _calculation(mass)
    if fuel < 0:
        return 0
    else:
        return fuel + total(fuel)
