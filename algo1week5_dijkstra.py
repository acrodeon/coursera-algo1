#################################################################################
#               Dijkstra's shortest-path algorithm                              #
# Weighted graph with 200 vertices labeled 1 to 200                             #
# Report the shortest-path distances to the following ten vertices              #
# in order: 7,37,59,82,99,115,133,165,188,197                                   #
#################################################################################

import sys
from vertex import Vertex
from graph import Graph
from dijkstra import DijkstraAlgo 

def readUndirectedGraph(filename):
    """build a Graph according to file as 6 as the first entry, "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200"""
    g = Graph()
    lines = open(filename).read().splitlines()
    for i in range(len(lines)):
        g.addVertex(i)
    for line in lines:
        # split in a list according to spaces
        data = line.split()
        # first element is the source node
        v = int(data[0])
        # each another element in list are adjacentVertex,edgeLength 
        for vertLength in data[1:]:
            w, length = vertLength.split(',')
            w = int(w)
            length = int(length)
            g.addEdge(v,w,length)
    return g


##################
# Main() to test #
##################
if __name__ == '__main__':
    g = readUndirectedGraph("dijkstraData.txt")
    dijAlgo = DijkstraAlgo(g)
    dijAlgo.computeShortPaths(g.getVertex(1))

    wanted = (7,37,59,82,99,115,133,165,188,197)
    for t in wanted:
        print(g.getVertex(t).getDistance(), end=',')
    print()
