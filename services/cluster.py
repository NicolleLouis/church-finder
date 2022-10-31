from services.distance import Distance


class ClusterService:
    @staticmethod
    def find_closest_cluster(point, clusters):
        if len(clusters) == 0:
            raise Exception("Should contain at least 1 cluster")

        position = point.position

        minimum_distance = Distance.euclidian(position, clusters[0].centroid)
        best_cluster = clusters[0]
        for cluster in clusters:
            distance = Distance.euclidian(position, cluster.centroid)
            if distance < minimum_distance:
                minimum_distance = distance
                best_cluster = cluster

        return best_cluster
