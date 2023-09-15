import math

from src.Figure import Figure


class Triangle(Figure):
    """Declare triangle params"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if type(side_a) != int or type(side_b) != int or type(side_c) != int:
            raise ValueError("Sides must be integers")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be greater, then zero")
        if side_a + side_b > side_c and side_a + side_c > side_b \
                and side_b + side_c > side_a:
            raise ValueError(
                "The length of side must be less, than the sum of the lengths"
                " two other sides")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a}, {side_b}, {side_c}"

    @property
    def get_area(self):
        return (self.side_a * self.side_b) / 2

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
