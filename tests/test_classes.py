from helpers.random_helper import random_big_side, random_small_side, \
    random_side, random_letters, random_punctuations, \
    random_whitespaces, random_bool, negative_side, random_float, random_int
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle

import pytest


class TestTriangle:
    """Testing triangle"""

    def test_valid_triangle(self):
        triangle = Triangle(5, 40, 40)

        assert triangle.name == f"Triangle {5}, {40}," \
                                f" {40}", \
            f"Incorrect name:{triangle.name}"
        assert round(triangle.get_area) == 100, "Wrong area"
        assert triangle.get_perimeter == 85, "Wrong perimeter"

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(random_punctuations(), random_punctuations(),
                               random_punctuations()),
                              (random_letters(), random_letters(),
                               random_letters()),
                              (random_whitespaces(), random_whitespaces(),
                               random_whitespaces()),
                              (random_bool(), random_bool(), random_bool()),
                              (0, 0, 0),
                              (negative_side(), negative_side(),
                               negative_side()),
                              (111, 1, 1)],
                             ids=["punctuations",
                                  "letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers",
                                  "one side less than the sum of the lengths"
                                  ])
    @pytest.mark.repeat(1)
    def test_invalid_triangle(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize("figure",
                             [Triangle(5, 40, 40),
                              Rectangle(random_side(), random_side()),
                              Square(random_side()),
                              Circle(random_int())],
                             ids=["Triangle", "Rectangle", "Square", "Circle"])
    def test_triangle_add_area(self, figure):
        triangle = Triangle(5, 40, 40)

        assert triangle.add_area(figure) == triangle.get_area \
               + figure.get_area, "Wrong area"


class TestRectangle:
    """Testing rectangle"""

    small_side = random_small_side(1, 9)
    big_side = random_big_side(10, 100)

    @pytest.mark.parametrize("side_a, side_b",
                             [(small_side,
                               small_side),
                              (big_side,
                               big_side)],
                             ids=["small sides",
                                  "big sides"])
    def test_valid_rectangle(self, side_a, side_b):
        rectangle = Rectangle(side_a, side_b)

        assert rectangle.name == f"Rectangle {side_a}, {side_b}", \
            f"Incorrect name:{rectangle.name}"
        assert rectangle.get_area == side_a * side_b, "Wrong"
        assert rectangle.get_perimeter == 2 * (side_a + side_b), \
            "Wrong perimeter"

    @pytest.mark.parametrize("side_a, side_b",
                             [(random_punctuations(), random_punctuations()),
                              (random_letters(), random_letters()),
                              (random_whitespaces(), random_whitespaces()),
                              (random_bool(), random_bool()),
                              (0, 0),
                              (negative_side(), negative_side())],
                             ids=["punctuations",
                                  "letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers"
                                  ])
    def test_invalid_rectangle(self, side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)

    @pytest.mark.parametrize("figure",
                             [Triangle(5, 40, 40),
                              Square(random_side()),
                              Circle(random_int())],
                             ids=["Triangle", "Square", "Circle"])
    def test_rectangle_add_area(self, figure):
        rectangle = Rectangle(random_side(), random_side())

        assert rectangle.add_area(figure) == rectangle.get_area \
               + figure.get_area, "Wrong area"


class TestSquare:
    """Testing square"""

    def test_valid_square(self):
        side = random_side()
        square = Square(side)

        assert square.name == f"Square {side}", \
            f"Incorrect name:{square.name}"
        assert square.get_area == side ** 2, "Wrong area"
        assert square.get_perimeter == side * 4, "Wrong perimeter"

    @pytest.mark.parametrize("side_a",
                             [random_punctuations(), random_letters(),
                              random_whitespaces(), random_bool(), 0,
                              negative_side()],
                             ids=["punctuations",
                                  "letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers"
                                  ])
    def test_invalid_square(self, side_a):
        with pytest.raises(ValueError):
            Square(side_a)

    @pytest.mark.parametrize("figure",
                             [Triangle(5, 40, 40),
                              Rectangle(random_side(), random_side()),
                              Square(random_side()),
                              Circle(random_int())],
                             ids=["Triangle", "Rectangle", "Square", "Circle"])
    def test_square_add_area(self, figure):
        square = Square(random_side())

        assert square.add_area(figure) == square.get_area \
               + figure.get_area, "Wrong area"


class TestCircle:
    """Testing circle"""

    @pytest.mark.parametrize("radius",
                             [random_float(), random_int()],
                             ids=["float", "integer"])
    def test_valid_circle(self, radius):
        import math

        circle = Circle(radius)

        assert circle.name == f"Circle with radius {radius}", \
            f"Incorrect name:{circle.name}"
        assert circle.get_area == math.pi * (radius ** 2), "Can't get area"
        assert circle.get_perimeter == 2 * math.pi * radius, \
            "Can't get perimeter"

    @pytest.mark.parametrize("radius",
                             [random_punctuations(),
                              random_letters(),
                              random_whitespaces(),
                              random_bool(),
                              0,
                              negative_side()],
                             ids=["punctuations",
                                  "letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers"])
    def test_invalid_circle(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize("figure",
                             [Triangle(5, 40, 40),
                              Rectangle(random_side(), random_side()),
                              Square(random_side()),
                              Circle(random_int())],
                             ids=["Triangle", "Rectangle", "Square", "Circle"])
    def test_circle_add_area(self, figure):
        circle = Circle(random_float())

        assert circle.add_area(figure) == circle.get_area \
               + figure.get_area, "Wrong area"
