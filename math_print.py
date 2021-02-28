#################################################################
# FILE : math_print.py
# WRITER : TSVIEL ZAIKMAN , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that prints Mathematical Functions using the Math Library
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################

# imports the Math library
import math
PI = math.pi
EULER = math.e


def golden_ratio():
    """The Golden Ratio Constant"""
    print ((1 + math.sqrt(5)) / 2)


def six_squared():
    """Six Squared Function"""
    print(6**2)


def hypotenuse():
    """Hypotenuse Function using Pythagorean triple"""
    print(math.sqrt((5**2) + (12**2)))


def pi():
    """print Pi Value Function"""
    print(PI)


def e():
    """Print Euler's Constant Value"""
    print(EULER)


def squares_area():
    """Print Squares area with sizes from 1 to 10"""
    print(1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2)


if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()