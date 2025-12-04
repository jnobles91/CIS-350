import heapq
import numpy as np


#from book
class Partition:
    """Union-find structure for maintaining disjoint sets."""

    # ------------------------- nested Position class -------------------------
    class Position:
        __slots__ = "_container", "_element", "_size", "_parent"

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group."""
            self._container = container      # reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self              # convention for a group leader

        @property
        def element(self):
            """Return element stored at this position."""
            return self._element

    # ------------------------- public Partition methods -------------------------
    def make_group(self, e):
        """Make a new group containing element e, and return its Position."""
        return self.Position(self, e)

    def find(self, p):
        """Find the group containing p and return the position of its leader."""
        if p._parent is not p:
            p._parent = self.find(p._parent)   # path compression
        return p._parent

    def union(self, p, q):
        """Merge the groups containing positions p and q (if distinct)."""
        a = self.find(p)
        b = self.find(q)
        if a is not b:                          # only merge if different groups
            # union by size
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size


# Edge class to represent a weighted edge
class Edge:
    def __init__(self, from_node, to, weight):
        self.from_node = from_node
        self.to = to
        self.weight = weight

# MinHeap (Priority Queue) implementation using heapq
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, distance, vertex):
        heapq.heappush(self.heap, (distance, vertex))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def empty(self):
        return len(self.heap) == 0

# Graph class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, from_node, to, weight):
        self.adj[from_node].append(Edge(from_node, to, weight))
        self.adj[to].append(Edge(to, from_node, weight))  # Undirected graph

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        pq = MinHeap()

        dist[src] = 0
        pq.push(0, src)

        while not pq.empty():
            u_dist, u = pq.pop()

            for edge in self.adj[u]:
                v, weight = edge.to, edge.weight

                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    pq.push(dist[v], v)

            print("Current shortest distances:", ["INF" if d == float('inf') else d for d in dist])

        print("\nFinal shortest distances from source", src, ":")
        for i in range(self.V):
            print(f"Vertex {i}: {'INF' if dist[i] == float('inf') else dist[i]}")
    
    #function to print adjacency matrix
    def print_adj_list(self):
        for v in range(self.V):
            #print each vertex number then print 
            print(f'Vertex: {v}')
            for edge in self.adj[v]:
                print(f'To {edge.to}, weight {edge.weight}')
            print()

    def prim_jarnik(self, start = 0):
        #skeleton from book, changed to fit this graph class

        d = {}
        tree = [] 
        pq = MinHeap() 
        pqlocator = {} 

        #initialize the distance map, root has distance 0, all others infinity
        for v in range(self.V):
            if v == start:
                #if vertex is starting vertex it's distance is 0                
                d[v] = 0
            else:
                #else distance is infinity, 
                d[v] = np.inf
            pqlocator[v] = pq.add(d[v], (v, None))

        while not pq.empty() and len(tree) < self.V - 1:
            key, value = pq.pop()
            u, edge = value          # unpack tuple from pq
            del pqlocator[u]         # u is no longer in pq

            if edge is not None:
                tree.append(edge)    # add edge to tree

            for link in g.incident_edges(u):
                v = link.opposite(u)
                if v in pqlocator:   # thus v not yet in tree
                    # see if edge (u, v) better connects v to the growing tree
                    wgt = link.element()
                    if wgt < d[v]:   # better edge to v?
                        d[v] = wgt   # update the distance
                        pq.update(pqlocator[v], d[v], (v, link))

        return tree
    
    def kruskal(self):

        #skeleton from book, adapted to graph class

        tree = []                         
        pq = MinHeap()          
        forest = Partition()              #position class from book
        position = {}                     
        total_weight = 0

        for v in range(self.V):
            #initialize groups of subtrees in the forest
            position[v] = forest.make_group(v)

        for vertex in self.adj:
            for edge in vertex:
                #add each edge in the graph to the heap
                if edge.from_node < edge.to:
                    pq.push(edge.weight, edge)

        
        while len(tree) != self.V - 1 and not pq.empty():
            #while tree is incomplete and edges remain, remove lowest edge as a candidate
            weight, edge = pq.pop()
            u, v = edge.from_node, edge.to
            a = forest.find(position[u])
            b = forest.find(position[v])
            if a != b:
                #if there is no cycle add to the tree
                tree.append(edge)
                forest.union(a, b)
                total_weight += weight
            print(f'Step: {len(tree) +  1}:')
            print(f'Current MST:')
            for edge in tree:
                print(f'From {edge.from_node}, To {edge.to}, Weight: {edge.weight}')
            
        print("Final MST by Kruskal's Algorithm: ")
        for edge in tree:
            print(f'From {edge.from_node}, To {edge.to}, Weight: {edge.weight}')
        return tree



# Main execution
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 3)
g.add_edge(3, 5, 2)
g.add_edge(4, 5, 6)

print("Executing Dijkstra's Algorithm using Min Heap...")
g.dijkstra(0)

#graph for problems
g = Graph(9)
g.add_edge(0, 1, 144)
g.add_edge(0, 2, 184)
g.add_edge(0, 3, 187)
g.add_edge(0, 6, 740)
g.add_edge(0, 7, 1391)
g.add_edge(0, 8, 1090)
g.add_edge(1, 6, 849)
g.add_edge(2, 6, 621)
g.add_edge(2, 8, 946)
g.add_edge(3, 6, 867)
g.add_edge(3, 5, 2704)
g.add_edge(3, 8, 1258)
g.add_edge(4, 5, 337)
g.add_edge(4, 7, 1235)
g.add_edge(4, 8, 2342)
g.add_edge(5, 6, 1846)
g.add_edge(5, 7, 1464)
g.add_edge(6, 7, 802)
g.add_edge(7, 8, 1121)


g.print_adj_list()
g.kruskal()