import graphviz


class Node:
    def __init__(self, num, obj=None):
        self.data = obj
        self.num = num


class Graph:
    def __init__(self):
        self.graph = dict()
        self.vertices = dict()

    def add_edge(self, e1, e2):
        self.vertices[e1.num] = e1
        self.vertices[e2.num] = e2

        if e1.num not in self.graph:
            self.graph[e1.num] = []

        self.graph[e1.num].append(e2.num)

    def is_linked(self, start):
        visited_list = self.dfs(start)

        for i in self.vertices:
            if i not in visited_list:
                return False

        return True

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
                # for j in visited:
                # print(j, end=' ')

                # print('')

        return comps_count

    def draw_graph(self, graph_name, extension):
        dot = graphviz.Graph(comment=graph_name, format=extension, engine='dot')
        for i in self.vertices:
            dot.node(str(i))

        for u in self.graph:
            for v in self.graph[u]:
                dot.edge(str(u), str(v))
        # print(dot.source)
        dot.render(graph_name)

g = Graph()
g.add_edge(Node(1), Node(2))
g.add_edge(Node(3), Node(4))
g.add_edge(Node(1), Node(4))
print(g.find_comps())
#g.draw_graph('lol', 'bmp')