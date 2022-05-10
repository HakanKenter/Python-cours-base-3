import math

class Point: 
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1
        
    def norm(self):
        n=math.sqrt(self.x**2 + self.y++2)
        return n

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
p1 = Point(2.0, 3.0)
p2 = Point(2.0, 3.0)
p3 = Point(2.0, 3.0)
print(p1.count)
print(p2.count)
print(Point.count)