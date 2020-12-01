import math


def is_even_number(number):
    return number % 2 == 0


def is_uneven_number(number):
    return number % 2 != 0


def is_perfect_square(number):
    sqrt = math.sqrt(number)
    return int(sqrt) == sqrt and number != 0
