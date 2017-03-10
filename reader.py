import Graph
import struct

class Reader:
  
  def read(file_path):
    vertices = set()
    edges_count = 0

    adj = []

    with open(file_path, "r") as f:
      for line in f:
        (edge1, edge2) = map(int, line.strip().split(' '))

        if edge1 not in adj:
          for i in range(len(adj), edge1+1):
            adj.append([])

        adj[edge1].append(edge2)

        vertices.add(edge1)
        vertices.add(edge2)
        edges_count += 1

    g = Graph.Graph(len(vertices), edges_count)

    for i in range(0, len(adj)):
      for j in adj[i]:
        print(i, j)
        g.add_edge(i, j)

    return g
