import graphviz


class Node:
    def __init__(self, num, obj=None):
	#Параметры узла
        self.data = obj
	#Номер узла
        self.num = num

	
class Graph:
    def __init__(self, directed=False):
	#список смежности
        self.graph = dict()
	#список вершин
        self.vertices = dict()
	#ориентированный граф или нет
        self.undirected = not directed
	#Начало пути в графе
        self.start = 0
	# конец пути
        self.finish = 0

    def add_node(self, e1):
	#Добовляем узел
        self.vertices[e1.num] = e1

    def add_edge(self, e1, e2):
    	#Добовляем вершины
	if e1 not in self.vertices:
            self.vertices[e1.num] = e1

        if e2 not in self.vertices:
            self.vertices[e2.num] = e2
	
	#Заполняем список смежности
        if e1.num not in self.graph:
            self.graph[e1.num] = []
	
        self.graph[e1.num].append(e2.num)
	#Если граф не ориентированый, добавляем обратное ребро
        if self.undirected:
            if e2.num not in self.graph:
                self.graph[e2.num] = []
            self.graph[e2.num].append(e1.num)

    def dfs(self, start, visited=None):
    #Поиск в глубину
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
	#Запускаем ДФС для каждой вершины в графе
        for i in self.vertices.keys():
            if i not in visited:
                visited = self.dfs(i, visited)
                comps_count += 1
        return comps_count

    def find_shortest_way(self, start, finish):
    #Поиск кратчайшего пути - алгоритм Дейкстры

        dist = [float('Inf') for i in range(len(self.graph.keys()) + 1)]   #Для всех вершин расстояние равно бесконечность
        parents = [[] for i in range(len(self.graph.keys()) + 1)]   #Для всех вершин задаем пустой список их предков
        pairs = []   #массив ребер кратчайшего пути
        dist[start] = 0   #расстояние до стартовой вершины равно 0
        visited = set()   #список посещенных вершин 
        for i in range(len(self.graph.keys()) + 1):   #бежим по всем вершинам графа
            v = -1   #v - вершина, в которую мы пойдем на этом шаге цикла
            for j in range(len(self.graph.keys()) + 1):   #цикл для поиска v - вершины, в которую мы пойдем. Она выбирается как ближайшая непосещенная вершина
                if j not in visited and (v == -1 or dist[j] < dist[v]):
                    v = j
            if dist[v] == float('Inf'):   #если расстояние до выбранной вершина оказывается равным бесконечности - останавливаем цикл 
                break
            visited.add(v)    #добавляем выбранную вершину в список посещенных
            if not self.graph.get(v):   #проверяем, если ли в списке смежности вершины v какие-либо вершины. Если нет, то останавливаем цикл
                break
            for j in self.graph.get(v):   #просматриваем все  смежные с v вершины и выпонляем "релаксации" - пытаемся уменьшить расстояния до них
                if dist[v] + 1 < dist[j]:    #если ресстояние до какий-либо смежной вершины удается уменьшить, то 
                    dist[j] = dist[v] + 1   #сохраняем результат с новым расстоянием
                    if v not in parents[j]:
                        parents[j].append(v)   #смежной вершине добавляем в качестве предка вершину v
                        parents[j] += (parents[v])   #а также всех предков v, чтобы корректно восстановить путь
        parents[finish].insert(0, finish)   #добавим в конец пути вершину finish (т.к. путь хранится в обратном порядке, добавляем ее в начало массива parents)
        prev = -1
        for j in parents[finish]:   #формируем пары вершин (т.е. ребра) пути для более удобной отрисовки
            if prev != -1:
                pairs.append([prev, j])
            prev = j
        return pairs   #возвращаем массив ребер кратчайшего пути

    def draw_graph(self, graph_name, extension, pairs=None):
    #Отрисовка графа
        drew = [] #массив уже отрисованных ребер
	#Проверка ориентированости
        if self.undirected:
            dot = graphviz.Graph(comment=graph_name, format=extension, engine='dot')
        else:
            dot = graphviz.Digraph(comment=graph_name, format=extension, engine='dot')
        dot.body.append('size=\"5,5!\"') #Размер графа
        for i in self.vertices:
            dot.node(str(i)) #Рисуем вершины
        for u in self.graph:
            for v in self.graph[u]:
                if self.undirected and [v, u] in drew:
                    continue
                drew.append([u, v])
                if pairs and ([v, u] in pairs or [u, v] in pairs):
		#Отрисовка пути
                    dot.edge(str(u), str(v), color='red')
                else:
		#Отрисовка ребер
                    dot.edge(str(u), str(v))
        dot.render(graph_name)
