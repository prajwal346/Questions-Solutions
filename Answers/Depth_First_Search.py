class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set() 
        self._dfs_util(start, visited)

    def _dfs_util(self, vertex, visited):
        visited.add(vertex)  
        print(vertex, end=' ')  

        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("DFS traversal starting from vertex 0:")
    g.dfs(3)
