from src.Figure import Figure


class Rectangle(Figure):
    """Declare rectangle params"""

    def __init__(self, side_a, side_b):
        super().__init__()
        if type(side_a) != int or type(side_b) != int:
            raise ValueError("Sides must be integers")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Sides must be greater, then zero")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Rectangle {side_a}, {side_b}"

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
