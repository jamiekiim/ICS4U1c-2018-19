'''
1. Define a class Rectangle that has attributes width and height defaulted to 0.
'''


class Rectangle():
    '''
    A class modelling wight and height
    '''

    def __init__(self):
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
    rect1 = Rectangle()
    rect1.width = float(input("Enter the width of the rectangle:"))
    rect1.height = float(input("Enter the height of the rectangle:"))

    print("The area of the rectangle is", get_area(rect1),".")

main()


