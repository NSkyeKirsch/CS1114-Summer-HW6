"""
Author: Noa Kirschbaum
Assignment / Part: HW6 - Q1
Date due: 2022-07-05
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


class TwoDShape:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return "2D Rectangle (rect1): {}x{}".format(self.width, self.height)

    def __add__(self, rhs):
        """
        DO NOT MODIFY EITHER OBJECT
        :param rhs: a new TwoDShape object
        :return: a new object with added height and width of both self and rhs
        """

    def __sub__(self, rhs):
        """
        DO NOT MODIFY EITHER OBJECT
        :param rhs: a new TwoDShape object
        :return: a new object, subtract rhs from self
        """

    def __lt__(self, rhs):
        """
        BOOLEAN, less than
        :param rhs: another TwoDShape object
        :return: True if area (WxH) self < rhs, False otherwise
        """

    def __gt__(self, rhs):
        """
        BOOLEAN, greater than
        :param rhs: another TwoDShape object
        :return: True if area (WxH) self > rhs, False otherwise
        """

    def __eq__(self, rhs):
        """
        BOOLEAN, equal
        :param rhs: another TwoDShape object
        :return: True if height and width values are the same
        """


def main():
    pass


if __name__ == "__main__":
    main()