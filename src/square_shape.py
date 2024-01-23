
class Shape:
    def area(self):
        print("Area of Shape by default is: ", 0)

class Square(Shape):

    def __init__(self, length):
        self.Shape = Shape
        self.length = length

    def area(self):
        print("Area of a Square is: ", self.length)

sq = Square(16)
sq.area()
sh = Shape()
sh.area()

'''Output
Area of a Square is:  16
Area of Shape by default is:  0
'''