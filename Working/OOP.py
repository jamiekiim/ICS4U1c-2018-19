class Rectangle():

    def _init_(self):
        self.width = 0
        self.height = 0

    def get_area(rec):
        """
        Computes the area of a rectangle
        :param rec: a Rectangle object
        :return:
        """

        return rec.width * rec.height

    def main():

        user width = float(input("Enter a width: "))
        user height = float(input("Enter a height: "))

        rect1 = Rectangle()
        rect1.width = user_width
        rect1.height = user_height

        area = rect1.width * rect1.height
        print("The area of the rectangle is", area) #or print("The area of the rectangle is" + str(area))

    main()