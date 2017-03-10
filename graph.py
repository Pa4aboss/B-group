import graphviz


class Node:
    def __init__(self, num, obj=None):
        #Параметры узла
        self.data = obj
        #Номер узла
        self.num = num

class Graph:
    def __init__(self):
        #список смежности
        self.graph = dict()
        #список вершин
        self.vertices = dict()
    
    def add_edge(self, e1, e2):
    #Добовляем вершины        
        self.vertices[e1.num] = e1
        self.vertices[e2.num] = e2

        #Заполняем список смежности
        if e1.num not in self.graph:
            self.graph[e1.num] = []

        self.graph[e1.num].append(e2.num)
        
    def dfs(self, start, visited=None):
    #Применяем поиск в глубину
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
    #Поиск связных компонентов
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
        #Отрисовываем граф
        dot = graphviz.Graph(comment=graph_name, format=extension, engine='dot')
        for i in self.vertices:
            dot.node(str(i))

        for u in self.graph:
            for v in self.graph[u]:
                dot.edge(str(u), str(v))
        # print(dot.source)
        dot.render(graph_name)
