#OO practice. Some parts shamelessly lifted from "How to think like a Computer Scientist" (ThinkPython)

#TODO - allow for initialising the point with a set of co-ords
#TODO - method to determine distance from origin
#TODO - create method to allow you to `print Point()` and have meaningful output
#TODO - allow to check if two points are equal using ==
#TODO - method `distance_from_point` to determine distance to another point
#TODO - method `move(dx, dy)` to move the given point by a set amount
#TODO - method to convert to polar co-ordinates
#TODO - allow for addition, subtraction and multiplication
#TODO - draw points (ASCII? canvas?)
#TODO - implement lines

class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        """ Create a new point at the origin """
        self.x = initX
        self.y = initY

    def __str__(self):
        return ("(%d,%d)" % (self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Line:
    def __init__(self, p1, p2):
        "p1 and p2 are Point type"
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return self.p1 + " " + self.p2

class Triangle:
    def __init__(self):
        pass

class Polygon:
    def __init__(self, points):
        "polygon is constructed in order of given points"



class Polygon:
    def __init__(self):


p = Point(3, 4)         # Instantiate an object of type Point
q = Point()         # and make a second point
print(p)
print(q)


print(p is q)