
class Graph:
	def __init__(self, vertices, edges):
		self.graph = []
		self.count_of_vertices = vertices
		self.count_of_edges = edges
		self.count_of_adj_vertices = []
		
		for i in range(self.count_of_vertices):
			self.graph.append([])
			self.count_of_adj_vertices.append(0)

	def add_edge(self, first_vertex, second_vertex):
		self.check_vertex(first_vertex)
		self.check_vertex(second_vertex)

		self.graph[first_vertex - 1].append(second_vertex)
		if first_vertex != second_vertex:
			self.graph[second_vertex - 1].append(first_vertex)
		self.count_of_adj_vertices[first_vertex - 1] += 1
		if first_vertex != second_vertex:
			self.count_of_adj_vertices[second_vertex - 1] += 1

	def check_vertex(self, vertex):
		if (vertex > self.count_of_vertices) or (vertex <= 0):
			print ("Error: Invalid parameter value")
			exit(0)
'''
	def print_graph(self):
		for i in range(self.count_of_vertices):
			print(i + 1, " ->", end = " ")
			for j in range(self.count_of_adj_vertices[i]):
				print(self.graph[i][j], " ->", end = " ")
			print (end="\n")
'''

'''
g = t_graph(6, 7)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 2)
g.add_edge(2, 4)
g.add_edge(1, 5)

g.print_graph()
'''
