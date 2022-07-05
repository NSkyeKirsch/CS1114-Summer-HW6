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
        return "2D Rectangle: {}x{}".format(self.width, self.height)

    def __add__(self, rhs):
        """
        DO NOT MODIFY EITHER OBJECT
        :param rhs: a new TwoDShape object
        :return: a new object with added height and width of both self and rhs
        """
        resulting_shape = TwoDShape(self.height + rhs.height, self.width + rhs.width)
        return resulting_shape

    def __sub__(self, rhs):
        """
        DO NOT MODIFY EITHER OBJECT
        :param rhs: a new TwoDShape object
        :return: a new object, subtract rhs from self
        """
        resulting_shape = TwoDShape(self.height - rhs.height, self.width - rhs.width)
        return resulting_shape

    def __lt__(self, rhs):
        """
        BOOLEAN, less than
        :param rhs: another TwoDShape object
        :return: True if area (WxH) self < rhs, False otherwise
        """
        if (self.width * self.height) < (rhs.width * rhs.height):
            return True
        else:
            return False

    def __gt__(self, rhs):
        """
        BOOLEAN, greater than
        :param rhs: another TwoDShape object
        :return: True if area (WxH) self > rhs, False otherwise
        """
        if (self.width * self.height) > (rhs.width * rhs.height):
            return True
        else:
            return False

    def __eq__(self, rhs):
        """
        BOOLEAN, equal
        :param rhs: another TwoDShape object
        :return: True if height and width values are the same
        """
        if self.height == rhs.height and self.width == rhs.width:
            return True
        else:
            return False


def main():
    rect1 = TwoDShape(5, 5)
    rect2 = TwoDShape(6, 6)
    rect3 = TwoDShape(11, 11)
    print("Object creation (rect1): ", rect1)
    print("Object creation (rect2): ", rect2)
    print("Object creation (rect3): ", rect3)

    sum_rect = rect1 + rect2
    print("Addition of rect1 + rect2 yields: ", sum_rect)

    print("Comparing rect3 with the result of rect1+rect2: ", end="")
    if rect3 == sum_rect:
        result = "the two rectangles are equal."
    else:
        result = "The two rectangles are NOT equal."
    print(result)

    rect3 = rect3 - rect2
    print("Subtracting rect2 from rect3 (rect3-rect2) yields: ", rect3)

    print('rect 3:', rect3)
    print('rect2:', rect2)
    if rect3 > rect2:
        result = "rect3 is greater than rect2."
    else:
        result = "rect3 is NOT greater than rect2."
    print(result)

    if rect3 < rect2:
        result = "rect3 is less than rect2."
    else:
        result = "rect3 is NOT less than rect2."
    print(result)


if __name__ == "__main__":
    main()