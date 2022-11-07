import matplotlib.pyplot as plt


class MapVisualisation:
    def __init__(self, map_instance):
        self.map_instance = map_instance

    def clusters(self):
        for cluster in self.map_instance.clusters:
            print(cluster)

    def graph(self):
        _fig, ax = plt.subplots()
        for cluster in self.map_instance.clusters:
            cluster.visualisation.plot(ax)

        plt.show()
