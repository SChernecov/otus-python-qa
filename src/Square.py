from src.Rectangle import Rectangle


class Square(Rectangle):
    """Declare square params"""

    def __init__(self, side):
        super().__init__(side, side)
        if type(side) != int:
            raise ValueError("Sides must be integers")
        if side <= 0:
            raise ValueError("Sides must be greater, then zero")
        self.side_a = side
        self.name = f"Square {side}"

    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return self.side_a * 4
