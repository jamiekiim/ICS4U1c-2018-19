class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self):
        '''
        Initialize the rectangle dimensions
        :return: None
        '''
        self.width = 0
        self.height = 0

def get_area(rec):
    """
    calculate the area of the rectangle
    @param width- width of the rectangle
    @param height- height of the rectangle
    @return: float- the calculated area of the rectangle
    """
    return rec.width*rec.height

def main():
    # first width and height
    rect1 = Rectangle()
    rect1.width = float(input("Enter the width of the first rectangle:"))
    rect1.height = float(input("Enter the height of the first rectangle:"))

    # second width and height
    rect2 = Rectangle()
    rect2.width = float(input("Enter the width of the second rectangle:"))
    rect2.height = float(input("Enter the height of the second rectangle:"))

    # third width and height
    rect3 = Rectangle()
    rect3.width = float(input("Enter the width of the third rectangle:"))
    rect3.height = float(input("Enter the height of the thid rectangle:"))

    # print out the areas of the three rectangles
    print("The area of the rectangle is", get_area(rect1), ".")
    print("The area of the rectangle is", get_area(rect2), ".")
    print("The area of the rectangle is", get_area(rect3), ".")
