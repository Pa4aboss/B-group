import graphviz


class Graph:
    def __init__(self, vertices, edges):
        self.graph = []
        self.count_of_vertices = vertices
        self.count_of_edges = edges
        self.vertex_degree = []

        for i in range(self.count_of_vertices):
            self.graph.append([])
            self.vertex_degree.append(0)

    def add_edge(self, first_vertex, second_vertex):
        self.check_vertex(first_vertex)
        self.check_vertex(second_vertex)
        # граф неориентированный
        # петель нет проверки не нужны
        # номера всех вершин сдвинуты на -1
        self.graph[first_vertex - 1].append(second_vertex - 1)
        self.graph[second_vertex - 1].append(first_vertex - 1)
        self.vertex_degree[first_vertex - 1] += 1
        self.vertex_degree[second_vertex - 1] += 1

    def check_vertex(self, vertex):
        if vertex in range(1, self.count_of_vertices + 1):
            print("Error: Invalid parameter value")
            exit(0)

    def print_graph(self):
        for i in range(self.count_of_vertices):
            print(i + 1, " ->", end=" ")
            for j in range(self.vertex_degree[i]):
                print(self.graph[i][j] + 1, " ->", end=" ")
            print(end="\n")

    # Надо добавить в переменную среды PATH строку "C:\Program Files (x86)\Graphviz(тут версия своя)\bin\",
    # иначе render не сработает
    def draw_graph(self, graph_name, extension):
        dot = graphviz.Graph(comment=graph_name, format=extension)
        for i in range(1, self.count_of_vertices + 1):
            dot.node("{}".format(i))
        for i in range(1, self.count_of_vertices + 1):
            for j in self.graph[i - 1]:
                dot.edge("{}".format(i), "{}".format(j + 1))
        # dot.render('output.gv')
        print(dot.source)

'''
g = Graph(6, 7)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 2)
g.add_edge(2, 4)
g.add_edge(1, 5)

g.print_graph()
g.draw_graph('pep','png')
'''