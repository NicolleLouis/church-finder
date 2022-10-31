class Position:
    def __init__(
            self,
            x: int,
            y: int,
    ):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({round(self.x, 2)}, {round(self.y, 2)})"

    def __eq__(self, other):
        if type(other) != Position:
            raise Exception(f"Can't compare a Position with {type(other)}")

        if other.x != self.x:
            return False

        if other.y != self.y:
            return False

        return True
