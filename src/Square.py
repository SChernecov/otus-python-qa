from src.Figure import Figure


class Square(Figure):
    """Declare square params"""

    def __init__(self, side_a, side_b, side_c, side_d):
        super().__init__()
        if type(side_a) != int or type(side_b) != int or type(
                side_c) != int or type(side_d) != int:
            raise ValueError("Sides must be integers")
        if side_a != side_c != side_b != side_d:
            raise ValueError("This is not a square")
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_d <= 0:
            raise ValueError("Sides must be greater, then zero")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d
        self.name = f"Square {side_a}, {side_b}, {side_c}, {side_d}"

    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return self.side_a * 4
