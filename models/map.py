from services.cluster import ClusterService
from services.map import MapService
from visualisation.map import MapVisualisation


class Map:
    x_min = None
    x_max = None
    y_min = None
    y_max = None
    has_changed = True
    turn_number = 0

    def __init__(self):
        self.points = []
        self.clusters = []
        self.service = MapService(self)
        self.visualisation = MapVisualisation(self)

    def add_point(self, point):
        self.points.append(point)

    def add_cluster(self, cluster):
        self.clusters.append(cluster)

    def fill_clusters(self):
        for point in self.points:
            cluster = ClusterService.find_closest_cluster(point, self.clusters)
            cluster.add_point(point)

    def empty_clusters(self):
        for cluster in self.clusters:
            cluster.reset_points()

    def run(self):
        while self.has_changed:
            print("######")
            self.service.iteration()
            self.visualisation.clusters()
            self.turn_number += 1
            print(self.turn_number)

    def set_boundaries(
            self,
            x_min,
            x_max,
            y_min,
            y_max,
    ):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def update_boundaries(self):
        self.x_min = min(map(lambda point: point.position.x, self.points))
        self.x_max = max(map(lambda point: point.position.x, self.points))
        self.y_min = min(map(lambda point: point.position.y, self.points))
        self.y_max = max(map(lambda point: point.position.y, self.points))

    def __str__(self):
        return f"{len(self.points)} points and {len(self.clusters)} clusters"
