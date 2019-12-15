import math

def _calculation(mass):
    """Calculates the amount of fuel required to launch"""
    return math.floor(mass / 3) - 2

def total(mass):
    """Returns the total amount fuel required"""
    fuel_weights = []
    while mass >= 0:
        mass = _calculation(mass)
        if mass > 1:
          fuel_weights.append(mass)
    return sum(fuel_weights)
