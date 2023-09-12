from src.Figure import Figure, ABC


class Triangle(Figure, ABC):
    """Declare triangle params"""

    def __init__(self, side_a, side_b, side_c, shape, height):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a}, {side_b}, {side_c}"
        self.shape = shape
        self.height = height

    @property
    def get_area(self):
        if self.shape == "rectangle_triangle":
            return self.get_area_rectangular_triangle()
        if self.shape == "isosceles_triangle":
            return self.get_area_isosceles_triangle(self.height)

    def get_area_rectangular_triangle(self):
        return (self.side_a * self.side_b) / 2

    def get_area_isosceles_triangle(self, height):
        return 1 / 2 * self.side_b * height
