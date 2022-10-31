import random

from models.cluster import Cluster
from models.position import Position


class MapService:
    def __init__(self, map_instance):
        self.map = map_instance

    def random_cluster(self):
        return Cluster(self.random_position())

    def random_position(self):
        x = random.randrange(self.map.x_min, self.map.x_max)
        y = random.randrange(self.map.y_min, self.map.y_max)
        return Position(x, y)

    def iteration(self):
        self.map.empty_clusters()
        self.map.fill_clusters()
        has_changed = True
        for cluster in self.map.clusters:
            cluster.update_centroid()
            has_changed &= cluster.has_changed
        self.map.has_changed = has_changed
