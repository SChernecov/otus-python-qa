from abc import ABC, abstractmethod


class Figure(ABC):
    """Declare figures methods"""

    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise AssertionError("Can't add area")
        return self.get_area() + other_figure.add_area