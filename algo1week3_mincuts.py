#################################################################################
#                         Algo1 Week3                                           #
# Karger's Algorithm for min-cut                                                #                      
#################################################################################

import random
import copy
import math

class Adjency:
    """Adjency list for a vertex and its adjacent vertices in the graph. Parallel edges are allowed"""
    def __init__(self,_vertex, _adjVertices=[]):
        """vertex is typically a string and adjVertices a list"""
        self.vertex = _vertex
        # dictionary to keep track of the vertices to which it is connected, and the weight of each edge
        self.adjVertices = _adjVertices
      
    def __str__(self):
        return str(self.vertex) + ' connectedTo: ' + str([x for x in self.adjVertices])

    def getConnections(self):
        """return all of the vertices that vertex is connected to"""
        return self.adjVertices()

class KargerGraph:
    """Undirected graph with adjency lists representation, parallel edges are allowed"""
    def __init__(self):
        """Adgency Lists representation of an undirected graph"""
        self.adjencies = {}

    def addAdjency(self, vertex, adjVertices):
        """add the adjency list of vertices adjacent to vertex"""
        self.adjencies[vertex] = adjVertices

    def removeVertex(self, vertex):
        """remove the adjacency list of vertex"""
        del self.adjencies[vertex]

    def getRandomEgde(self):
        """randomly pick one edge and return it as tuple (u,v)"""
        u = list(self.adjencies.keys())[random.randint(0, len(self.adjencies.keys())-1)]
        # u must have at least one adjacent vertex otherwise raise IndexError
        v = random.choice(self.adjencies[u])
        return (u,v)

    def contract(self, u, v):
        """contraction according to edge (u,v) as only vertex u and deletion of loop on u"""
        # adjacent nodes of v are now adjacent to u
        self.adjencies[u].extend(self.adjencies[v])
        # v is replaced by u in adjacency list of adjacent nodes of v
        for w in self.adjencies[v]:
            for i in range(0, len(self.adjencies[w])):
                if self.adjencies[w][i] == v:
                    self.adjencies[w][i] = u
        # remove loops (if any) on u
        while u in self.adjencies[u]:
            self.adjencies[u].remove(u)
        # delete adjacency list relevant to v
        self.removeVertex(v)

    def cloneGraph(self):
        """return a clone of this graph"""
        g = KargerGraph()
        g.adjencies = copy.deepcopy(self.adjencies)
        return g
    
    def getNbVertices (self):
        """ return the number n of vertices"""
        return len(self.adjencies.keys())

    def getCutSize(self):
        """return the number of egdes incident to first vertex"""
        return len(list(self.adjencies.values())[0])

class KargerAlgo:
    """Ramdom Contraction Algorithm from Karger to compute min cut with probability of failure lower than 1 / nb of vertices"""
    def __init__(self):
        """Adgency Lists representation of an undirected graph"""
        self.adjencies = {}

    def kargerAlgo(self, G):
        """one instance of Karger's Algorithm to return the size of a cut in graph G"""
        # clone the graph to always start trials from original graph G
        cloneG = G.cloneGraph()
        while (cloneG.getNbVertices() > 2):
            u,v = cloneG.getRandomEgde()
            cloneG.contract(u,v)
        return cloneG.getCutSize()

    def multipleKargerAlgo(self, G):
        """n**2 * ln(n) instances of basic Karger Algo"""
        n = G.getNbVertices()
        nbIterations = math.pow(n,2) * math.log(n)
        nbIterations = math.ceil(nbIterations)
        res = self.kargerAlgo(G)
        for trial in range(1, nbIterations):
            trialRes = self.kargerAlgo(G)
            print(trial, trialRes, res)
            if trialRes < res :
                res = trialRes
        return res


        
##################
# Main() to test #
##################
if __name__ == '__main__':
##    G = KargerGraph()
##    G.addAdjency("a", ["b", "d"])
##    G.addAdjency("b", ["a", "c", "d"])
##    G.addAdjency("c", ["b", "d"])
##    G.addAdjency("d", ["a", "b", "c"])
##
    A = KargerAlgo()
##    print("Min cut is {}".format(A.multipleKargerAlgo(G)))

    f = open(file="kargerMinCut.txt", mode="r")
    # all lines are saved in a list
    lines = f.read().splitlines()
    f.close()
    
    G = KargerGraph()
    for line in lines:
        # each element are separated by '\t' in line, and '' at the end for the last '\t'
        # '200\t149\t155\t52\t87\t120\t39\t160\t137\t27\t79\t131\t100\t25\t55\t23\t126\t84\t166\t150\t62\t67\t1\t69\t35\t' for example
        lst = line.split('\t')
        G.addAdjency(lst[0], lst[1:-1])
    print("Min cut is {}".format(A.multipleKargerAlgo(G)))
    
    

        
    
    
        

    
        
            
            
                
        
        
