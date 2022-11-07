from services.barycenter import Barycenter
from visualisation.cluster import ClusterVisualisation


class Cluster:
    def __init__(
            self,
            centroid_position
    ):
        self.centroid = centroid_position
        self.points = []
        self.has_changed = True
        self.visualisation = ClusterVisualisation(self)

    def __str__(self):
        return f"centroid: {self.centroid} ({len(self.points)} points)"

    def add_point(self, point):
        self.points.append(point)

    def reset_points(self):
        self.points = []

    def update_centroid(self):
        new_centroid = Barycenter.find(self.positions())
        self.has_changed = new_centroid != self.centroid
        self.centroid = new_centroid

    def positions(self):
        return list(
            map(
                lambda point: point.position,
                self.points
            )
        )
