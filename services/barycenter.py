from models.position import Position


class Barycenter:
    @staticmethod
    def find(positions):
        if len(positions) == 0:
            raise "Can't compute a barycenter of zero points"
        total_x = sum(map(lambda position: position.x, positions))
        x = total_x/len(positions)
        total_y = sum(map(lambda position: position.y, positions))
        y = total_y/len(positions)
        return Position(x, y)
