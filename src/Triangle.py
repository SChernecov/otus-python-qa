import math

from src.Figure import Figure, ABC


class Triangle(Figure, ABC):
    """Declare triangle params"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if type(side_a) != int or type(side_b) != int or type(side_c) != int:
            raise ValueError("Sides must be integers")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be greater, then zero")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a}, {side_b}, {side_c}"

    @property
    def get_area(self):
        if self.side_a == self.side_b:
            height = math.sqrt(self.side_a ** 2 - (self.side_b / 2) ** 2)
            return self.get_area_isosceles_triangle(height)
        if self.side_a != self.side_b:
            return self.get_area_rectangular_triangle()

    def get_area_rectangular_triangle(self):
        return (self.side_a * self.side_b) / 2

    def get_area_isosceles_triangle(self, height):
        return 1 / 2 * self.side_b * height

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
