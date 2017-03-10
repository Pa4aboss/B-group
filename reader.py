from graph import Graph, Node
import struct
import re


class Reader:
    def read(file_path):
        g = Graph()

        with open(file_path, "r") as f:
            lines = [line for line in f]
            u, v = map(int, lines[0].strip().split(' '))
            for i in range(1, u + 1):
                g.add_node(Node(i))
            for i in range(1, v + 1):
                (edge1, edge2) = map(int, lines[i].strip().split(' '))
                g.add_edge(Node(edge1), Node(edge2))
            g.start, g.finish = map(int, lines[len(lines) - 1].strip().split(' '))
        return g
