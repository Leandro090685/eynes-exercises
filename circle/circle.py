import math

class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un valor positivo y mayor que cero.")
        self._radius = radius
        