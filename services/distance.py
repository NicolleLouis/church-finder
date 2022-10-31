import math


class Distance:
    @staticmethod
    def euclidian(position1, position2):
        x = (position1.x - position2.x)**2
        y = (position1.y - position2.y)**2
        return math.sqrt(x + y)
