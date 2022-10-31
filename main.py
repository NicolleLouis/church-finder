from generator.map import MapGenerator

map_instance = MapGenerator(
    size=100,
    number_of_points=100,
    number_of_clusters=3
).map_instance
map_instance.run()
