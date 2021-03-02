class Node:
    def __init__(self, point):
        self.point = point

    def __repr__(self):
        return f'Node({self.point})'


class Graph:
    def __init__(self, adj_matrix=None):
        """
        Create Graph object by adjacency matrix, or without any param create empty Graph object
        :param adj_matrix: it is adjacency matrix, where elements is weight of edge if it not zero
        """
        adj_matrix = [] if adj_matrix is None else adj_matrix
        self.vertex = {i + 1: Node(i+1) for i in range(len(adj_matrix))}
        # since the matrix is symmetric about the main diagonal, it is sufficient to process one diagonal half
        self.edge = {(i+1, i+j+1): elem for i, row in enumerate(adj_matrix) for j, elem in enumerate(row[i:]) if elem}
        # since graph is not directed (i, j) edge is same to (j, i)
        union = sorted(list(self.edge.keys()) + [item[::-1] for item in self.edge])
        self.neighbours = {node: {elem for my_node, elem in union if my_node == node} for node, other in union}

    def add_vertex(self, i):
        if i in self.vertex:
            raise Exception(f'Node({i}) already exist')
        self.vertex.update({i: Node(i)})
        self.neighbours.update({i: set()})

    def delete_vertex(self, i):
        if i not in self.vertex:
            raise Exception(f'Node({i}) does not exist')
        self.vertex.pop(i)
        self.edge = {k: v for k, v in self.edge.items() if i not in k}
        self.neighbours.pop(i)
        for key, value in self.neighbours.items():
            self.neighbours[key].discard(i)

    def add_edge(self, i, j, weight=None):
        if i not in self.vertex:
            self.add_vertex(i)
        if j not in self.vertex:
            self.add_vertex(j)
        if (i, j) not in self.edge and (j, i) not in self.edge:
            self.edge.update({(i, j): weight})
            self.neighbours[i].add(j)
            self.neighbours[j].add(i)
        else:
            if (i, j) in self.edge:
                self.edge[(i, j)] = weight
            else:
                self.edge[(j, i)] = weight

    def __contains__(self, other_graph):
        return set(self.edge.keys()).issuperset(set(other_graph.edge.keys())) \
               and set(self.vertex.keys()).issuperset(set(other_graph.vertex.keys()))

    def __repr__(self):
        return f'Graph({set(self.vertex.keys())}:{list(self.edge.keys())})'
