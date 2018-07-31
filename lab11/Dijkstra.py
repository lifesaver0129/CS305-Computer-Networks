# This is the initial open-on function, which called the real dijk function I wrote
def dijkstra(graph, src):
    if graph is None:
        return None
    graphclass = Graph(graph)
    distance, path = dij_use_graph(graphclass, src)
    path = get_path(path, src)
    forwarding_table = get_ft(path, src)
    return distance, path, forwarding_table

# The graph file which use to store the data from imput 2 dimension list
class Graph:
    nodes = set()
    edges = []
    distances = {}

    # The init function that used to creat the graph
    def __init__(self, graph_list):
        for i in range(0, len(graph_list)):
            self.add_node(i)
        for i in range(0, len(graph_list)):
            for j in range(i, len(graph_list)):
                if graph_list[i][j] == float('inf') or i == j:
                    pass
                else:
                    self.add_edge(i, j, graph_list[i][j])

    # Used to add node and edge of the graph
    def add_node(self, value):
        self.nodes.add(value)
        self.edges.append([])

    # Used to add the weight of each edge
    def add_edge(self, from_node, to_node, dist):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = dist

# The true dijkstra method process
def dij_use_graph(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    # When there's still node exists
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        # update each edge
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min(min_node, edge), max(min_node, edge))]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

# Get the first step of each way from initial node
def get_ft(ori_path, src):
    new_path = {}
    for key in ori_path:
        if key == src:
            pass
        else:
            new_path[key] = ori_path[key][0:2]
    return new_path

# Print the graph of each node from initial node
def get_path(ori_path, src):
    new_path = {}
    for key in ori_path:
        new_path[key] = [key]
        curr_point = key
        while src not in new_path[key]:
            new_path[key].insert(0, ori_path[curr_point])
            curr_point = ori_path[curr_point]
    new_path[src] = [src]
    return new_path

# The main starting function
if __name__ == '__main__':
    graph_list = [[0, 7, float('inf'), 3, 3, 2],
                  [7, 0, 5, float('inf'), 1, 2],
                  [float('inf'), 5, 0, 6, float('inf'), 3],
                  [3, float('inf'), 6, 0, float('inf'), 1],
                  [3, 1, float('inf'), float('inf'), 0, float('inf')],
                  [2, 2, 3, 1, float('inf'), 0]]

    distance, path, forwarding_table = dijkstra(graph_list, 3)  # 查找从源点3开始到其他节点的最短路径
    print(distance)
    print(path)
    print(forwarding_table)
