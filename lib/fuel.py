import math

def calculator(mass):
    """Calculates the amount of fuel required to launch a module"""
    return math.floor(mass / 3) - 2