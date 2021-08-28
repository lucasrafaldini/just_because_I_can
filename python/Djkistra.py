



class Djkistra:
    """
    Djikstra's algorithm
    """

    def __init__(self, graph):
        self.graph = graph
        self.nodes = graph.nodes
        self.edges = graph.edges
        self.distances = {}
        self.visited = {}
        self.path = {}
        self.path_cost = {}

    def _init_distances(self):
        for node in self.nodes:
            self.distances[node] = float('inf')
            self.visited[node] = False

    def _init_path(self):
        for node in self.nodes:
            self.path[node] = None
            self.path_cost[node] = float('inf')

    def _init_distances_from_source(self, source):
        self.distances[source] = 0

    def _init_visited(self, source):
        self.visited[source] = True

    def _init_path_from_source(self, source):
        self.path[source] = source

    def _init_path_cost(self, source):
        self.path_cost[source] = 0

    def _update_distances(self, node, distance):
        if distance < self.distances[node]:
            self.distances[node] = distance

    def _update_path(self, node, parent):
        if self.path[node] is None:
            self.path[node] = parent

    def _update_path_cost(self, node, cost):
        if cost < self.path_cost[node]:
            self.path_cost[node] = cost

    def _update_visited(self, node):
        self.visited[node] = True

    def _is_visited(self, node):
        return self.visited[node]

    def _is_unvisited(self, node):
        return not self._is_visited(node)

    def _is_unvisited_and_lower_than_distances(self, node):
        return self._

