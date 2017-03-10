import graphviz


class Node:
    def __init__(self, num, obj=None):
        self.data = obj
        self.num = num


class Graph:
    def __init__(self, directed=False):
        self.graph = dict()
        self.vertices = dict()
        self.undirected = not directed
        self.start = 0
        self.finish = 0

    def add_node(self, e1):
        self.vertices[e1.num] = e1

    def add_edge(self, e1, e2):
		if e1 not in self.vertices:
            self.vertices[e1.num] = e1

        if e2 not in self.vertices:
            self.vertices[e2.num] = e2

        if e1.num not in self.graph:
            self.graph[e1.num] = []

        self.graph[e1.num].append(e2.num)
        if self.undirected:
            if e2.num not in self.graph:
                self.graph[e2.num] = []
            self.graph[e2.num].append(e1.num)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = []

        visited.append(start)

        if start not in self.graph:
            return visited

        for u in self.graph[start]:
            if u not in visited:
                self.dfs(u, visited)

        return visited

    def find_comps(self):
        visited = []

        comps_count = 0

        for i in self.vertices.keys():
            if i not in visited:
                visited = self.dfs(i, visited)
                comps_count += 1
        return comps_count

    def find_shortest_way(self, start, finish):
        dist = [float('Inf') for i in range(len(self.graph.keys()) + 1)]
        parents = [[] for i in range(len(self.graph.keys()) + 1)]
        pairs = []
        dist[start] = 0
        visited = set()
        for i in range(len(self.graph.keys()) + 1):
            v = -1
            for j in range(len(self.graph.keys()) + 1):
                if j not in visited and (v == -1 or dist[j] < dist[v]):
                    v = j
            if dist[v] == float('Inf'):
                break
            visited.add(v)
            if not self.graph.get(v):
                break
            for j in self.graph.get(v):
                if dist[v] + 1 < dist[j]:
                    dist[j] = dist[v] + 1
                    if v not in parents[j]:
                        parents[j].append(v)
                        parents[j] += (parents[v])
        parents[finish].insert(0, finish)
        prev = -1
        for j in parents[finish]:
            if prev != -1:
                pairs.append([prev, j])
            prev = j
        return pairs

    def draw_graph(self, graph_name, extension, pairs=None):
        drew = []
        if self.undirected:
            dot = graphviz.Graph(comment=graph_name, format=extension, engine='dot')
        else:
            dot = graphviz.Digraph(comment=graph_name, format=extension, engine='dot')
        dot.body.append('size=\"5,5!\"')
        for i in self.vertices:
            dot.node(str(i))
        for u in self.graph:
            for v in self.graph[u]:
                if self.undirected and [v, u] in drew:
                    continue
                drew.append([u, v])
                if pairs and ([v, u] in pairs or [u, v] in pairs):
                    dot.edge(str(u), str(v), color='red')
                else:
                    dot.edge(str(u), str(v))
        dot.render(graph_name)
