import math

class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un valor positivo y mayor que cero.")
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un valor positivo y mayor que cero.")
        self._radius = radius

    def get_area(self):
        return math.pi * self._radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self._radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("La multiplicación solo está permitida por números positivos y mayores que cero.")
        return Circle(self._radius * n)

    def __str__(self):
        return f"Círculo de radio {self._radius}"