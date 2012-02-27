from math import sin, cos, pi, atan2


class Point(object):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    @property
    def x(self):
        return round(self.r * cos(self.theta))

    @x.setter
    def x(self, val):
        self.r = round(((val * val) + (self.y * self.y)) ** 0.5)
        self.theta = round(atan2(self.y, val))

    @property
    def y(self):
        return round(self.r * sin(self.theta))

    def rotate(self, theta):
        self.theta += theta

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
    # right!
    # now try setting y...
