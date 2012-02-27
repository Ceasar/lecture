from math import sin, cos, pi


class Point(object):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta
        self.setup()

    def setup(self):
        self.x = round(self.r * cos(self.theta))
        self.y = round(self.r * sin(self.theta))

    def rotate(self, theta):
        self.theta += theta
        self.setup()

    def __str__(self):
        return "x = %s; y = %s; r = %s; theta = %s;" % (self.x, self.y, self.r, self.theta)


if __name__ == "__main__":
    p = Point(1, pi / 2)
    print p
    p.rotate(pi / 2)
    print p
    # so far so good
    p.x = 10
    print p
    # wrong!
