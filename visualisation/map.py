class MapVisualisation:
    def __init__(self, map_instance):
        self.map_instance = map_instance

    def clusters(self):
        for cluster in self.map_instance.clusters:
            print(cluster)
