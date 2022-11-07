class ClusterVisualisation:
    def __init__(self, cluster):
        self.cluster = cluster

    def plot(self, ax):
        x = list(map(lambda point: point.position.x, self.cluster.points))
        y = list(map(lambda point: point.position.y, self.cluster.points))
        ax.scatter(x, y)
