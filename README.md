# graph-model

A graph is a pair G = (V, E), where V is a set whose elements are called vertices (singular: vertex), and E is a set of paired vertices, whose elements are called edges (sometimes links or lines).

For example we have V={1, 2, 3} 
-  ```E = [(1,2), (3,1]]```
- graph  ```G = (V,  E)```

##### Simple graph do not have multiple edges and loops and graph is undirected graph. 
- multiple edges means graph E can be ```[(1,2), (1, 2), (3, 1)]```
- graph has loops means graph can have ```E = [(1, 1), (1, 2), (3, 1)]```.
- graph is directed means edge ```(1, 2)``` and ```(2, 1)``` are different edges
- weighted graph means for every edge is assigned number(weight)

###### For this homework we will consider that graph is simple undirected weighted graph.

More information: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)


Implement Graph module as following:

1. Consider graph's vertices as Nodes and create class Note which will indicate graph's vertices

2. Graph class should has attributes 
   - Edge dict
   - Vertex dict
   - Neighbours dict
   
   for example graph G in the begining of file 
       - ```Edges = {(1, 2) : 2, (3, 1): 4}```, where 2 and for are weights of ```(1, 2)```, ```(3, 1)``` edges
       - ```Vertives = {1, Node(1), 2: Node(2), 3: Node(3)}```
       - ```Neighbours = {1: {2, 3}, 2: {1}, 3: {1}}```
    
 2. has method ```add_vertex(self, i)``` ---- creates Node for vertex if vertex doesn't exist in vertex list of Graph, and add neighbour set in Neighbours dict
 3. has method ```delete_vertex(self, i)``` ---- deletes vertex from Vertex dict, delete edges of that vertex and delete neighbours and delete from neighbours list from Neighbours dict
 4. has method ```add_edge(self, i, j, weight=None)``` ----- adds edge with vertices i, j, and assigns weight if Graph is weighted, and updates List, Neighbours dicts for i, j vertices and (i, j) line. If some of vertices doesn't exists creates one.
   
 5. has ```__contains__(self, graph_2)``` method
    ```graph_2 in graph_1``` or  ```graph_1.__contains__(graph_2)``` should check if nodes of graph_2 contains in nodes of graph_1 and edges of graph_2 contains in edges of graph_1
    
