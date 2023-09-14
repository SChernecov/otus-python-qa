from helpers.random_helper import random_big_side, random_small_side, \
    random_triangle_side, random_lower_letters, random_punctuations, \
    random_whitespaces, random_bool, negative_side
from src.Rectangle import Rectangle
from src.Triangle import Triangle

import pytest


class TestIsoscelesTriangle:
    """Testing isosceles rectangle"""

    isosceles_triangle_side = random_triangle_side()

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(isosceles_triangle_side,
                               isosceles_triangle_side,
                               random_small_side()),
                              (isosceles_triangle_side,
                               isosceles_triangle_side,
                               random_big_side()
                               )],
                             ids=[
                                 "two isosceles triangle sides with one small",
                                 "two isosceles triangle sides with one big"
                             ])
    def test_valid_rectangular_triangle(self, side_a, side_b, side_c):
        isosceles_triangle = Triangle(side_a, side_b, side_c)

        assert isosceles_triangle.name == f"Triangle {side_a}, {side_b}," \
                                          f" {side_c}", \
            f"Incorrect name:{isosceles_triangle.name}"
        assert isosceles_triangle.get_area, \
            f"Incorrect area:{isosceles_triangle.get_area}"
        assert isosceles_triangle.get_perimeter, \
            f"Incorrect perimeter:{isosceles_triangle.get_perimeter}"

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(random_punctuations(), random_punctuations(),
                               random_punctuations()),
                              (random_lower_letters(), random_lower_letters(),
                               random_lower_letters()),
                              (random_whitespaces(), random_whitespaces(),
                               random_whitespaces()),
                              (random_bool(), random_bool(), random_bool()),
                              (0, 0, 0),
                              (negative_side(), negative_side(),
                               negative_side())],
                             ids=["punctuations",
                                  "lower_letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers"
                                  ])
    def test_invalid_rectangular_triangle(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)


class TestRectangularTriangle:
    """Testing rectangular triangle"""

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(random_small_side(), random_small_side(),
                               random_small_side()),
                              (random_big_side(), random_big_side(),
                               random_big_side()),
                              (random_triangle_side(), random_triangle_side(),
                               random_triangle_side())],
                             ids=["small sides",
                                  "big sides",
                                  "big and small sides"])
    def test_valid_isosceles_triangle(self, side_a, side_b, side_c):
        rectangular_triangle = Triangle(side_a, side_b, side_c)

        assert rectangular_triangle.name == f"Triangle {side_a}, {side_b}," \
                                            f" {side_c}", \
            f"Incorrect name:{rectangular_triangle.name}"
        assert rectangular_triangle.get_area, \
            f"Incorrect area:{rectangular_triangle.get_area}"
        assert rectangular_triangle.get_perimeter, \
            f"Incorrect perimeter:{rectangular_triangle.get_perimeter}"

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(random_punctuations(), random_punctuations(),
                               random_punctuations()),
                              (random_lower_letters(), random_lower_letters(),
                               random_lower_letters()),
                              (random_whitespaces(), random_whitespaces(),
                               random_whitespaces()),
                              (random_bool(), random_bool(), random_bool()),
                              (0, 0, 0),
                              (negative_side(), negative_side(),
                               negative_side())],
                             ids=["punctuations",
                                  "lower_letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers"
                                  ])
    def test_invalid_isosceles_triangle(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)


class TestRectangle:
    """Testing rectangle"""

    rectangle_small_side_a_and_side_c = random_small_side()
    rectangle_small_side_b_and_side_d = random_small_side()

    rectangle_big_side_a_and_side_c = random_big_side()
    rectangle_big_side_b_and_side_d = random_big_side()

    @pytest.mark.parametrize("side_a, side_b, side_c, side_d",
                             [(rectangle_small_side_a_and_side_c,
                               rectangle_small_side_b_and_side_d,
                               rectangle_small_side_a_and_side_c,
                               rectangle_small_side_b_and_side_d),
                              (rectangle_big_side_a_and_side_c,
                               rectangle_big_side_b_and_side_d,
                               rectangle_big_side_a_and_side_c,
                               rectangle_big_side_b_and_side_d),
                              (rectangle_small_side_a_and_side_c,
                               rectangle_big_side_b_and_side_d,
                               rectangle_small_side_a_and_side_c,
                               rectangle_big_side_b_and_side_d)],
                             ids=["small sides",
                                  "big sides",
                                  "big and small sides"])
    def test_valid_rectangle(self, side_a, side_b, side_c, side_d):
        rectangle = Rectangle(side_a, side_b, side_c, side_d)

        assert rectangle.name == f"Rectangle {side_a}, {side_b}, {side_c}," \
                                 f" {side_d}", \
            f"Incorrect name:{rectangle.name}"
        assert rectangle.get_area, \
            f"Incorrect area:{rectangle.get_area}"
        assert rectangle.get_perimeter, \
            f"Incorrect perimeter:{rectangle.get_perimeter}"

    @pytest.mark.parametrize("side_a, side_b, side_c, side_d",
                             [(random_punctuations(), random_punctuations(),
                               random_punctuations(), random_punctuations()),
                              (random_lower_letters(), random_lower_letters(),
                               random_lower_letters(), random_lower_letters()),
                              (random_whitespaces(), random_whitespaces(),
                               random_whitespaces(), random_whitespaces()),
                              (random_bool(), random_bool(), random_bool(),
                               random_bool()),
                              (0, 0, 0, 0),
                              (negative_side(), negative_side(),
                               negative_side(), negative_side()),
                              (random_small_side(), random_small_side(),
                               random_small_side(), random_small_side())],
                             ids=["punctuations",
                                  "lower_letters",
                                  "whitespaces",
                                  "boolean",
                                  "zero",
                                  "negative numbers",
                                  "equal sides"
                                  ])
    def test_invalid_rectangle(self, side_a, side_b, side_c, side_d):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b, side_c, side_d)


class TestSquare:
    """Testing square"""
    pass


class TestCircle:
    """Testing circle"""
    pass
