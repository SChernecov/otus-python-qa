import math

from src.Figure import Figure


class Circle(Figure):
    """Declare circle params"""

    def __init__(self, radius):
        super().__init__()
        if type(radius) != float and type(radius) != int:
            raise ValueError("Radius must be float or int")
        if radius <= 0:
            raise ValueError("Radius must be greater, then zero")
        self.radius = radius
        self.name = f"Circle with radius {radius}"

    @property
    def get_area(self):
        return math.pi * (self.radius ** 2)

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.radius
