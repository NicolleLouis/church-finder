from models.map import Map
from models.point import Point
from services.map import MapService


class MapGenerator:
    def __init__(self, number_of_clusters: int, number_of_points: int, size: int):
        self.number_of_clusters: int = number_of_clusters
        self.number_of_points: int = number_of_points
        self.size: int = size

        self.map_instance = Map()
        self.map_service = MapService(map_instance=self.map_instance)
        self.generate()

    def generate(self):
        self.map_instance.set_boundaries(
            x_min=0,
            x_max=self.size,
            y_min=0,
            y_max=self.size,
        )
        self.add_points()
        self.map_instance.update_boundaries()
        self.add_clusters()

    def add_points(self):
        for _ in range(self.number_of_points):
            random_position = self.map_service.random_position()
            self.map_instance.add_point(Point(random_position))

    def add_clusters(self):
        for _ in range(self.number_of_clusters):
            random_cluster = self.map_service.random_cluster()
            self.map_instance.add_cluster(random_cluster)
