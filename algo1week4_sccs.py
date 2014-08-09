#################################################################################
#                         Algo1 Week4                                           #
# stronglyConnectedComponents                                                   #                      
#################################################################################
import os
import threading
import sys
from stack import Stack

class DFSNode:
    """Adjency list for a vertex and its adjacent vertices in the graph. Parallel edges are allowed"""
    def __init__(self, id):
        """vertex is typically a string and adjVertices a list"""
        self.vertex = id
        # adjency list of the vertices to which it is connected
        self.adjVertices = []
        # finishing time
        self.time = id
        # if node has been explored during DFS
        self.explored = False

    def setFinish(self, time):
        """set the finishing time in DFS"""
        self.finish = time

    def getFinish(self):
        """return the finishing time in DFS"""
        return self.finish

    def setExplored(self, status):
        """node has been explored or not, status is True or False"""
        self.explored = status

    def isExplored(self):
        """return True if node has already been considered in DFS"""
        return self.explored
    
    def getConnections(self):
        """return all of the vertices that vertex is connected to"""
        return self.adjVertices

    def addNeighbor(self,nbrNode):
        """add a connection from this vertex to another"""
        self.adjVertices.append(nbrNode)

    def getId(self):
        """returns the label (e.g. integer)"""
        return self.vertex


class DFSGraph:
    """Directed graph with adjency lists representation"""
    def __init__(self):
        """creates a new, empty graph"""
        # a dictionary that maps vertex names to vertex objects
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        """adds and returns an instance of DFSNode to the graph"""
        self.numVertices = self.numVertices + 1
        newVertex = DFSNode(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        """finds and return the vertex named n in the graph or None"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        """True if the given vertex is in the graph, False otherwise"""
        return n in self.vertList

    def addEdge(self,f,t):
        """adds a new directed edge 'f' -> 't' to the graph"""
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        else:
            nv = self.vertList[t]
        self.vertList[f].addNeighbor(nv)

    def getVertices(self):
        """returns the list of all vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """to iterate over all the vertex objects in a particular graph"""
        return iter(self.vertList.values())

    def transpose(self, transG):
        """transG filled as the transpose graph where all the edges in the graph have been reversed"""
        for v in self:
            for w in v.getConnections():
                transG.addEdge(w.getId(), v.getId())

class KosarajuAlgo:
    """SCCs Algorithm from Kosaraju to compute strongly connected component of a directed graph"""
    def __init__(self):
        """Global variables for finishing time and leader, dictionary of sccs"""
        self.finishingTime = 0
        # leader as key for each scc
        self.sccs = {}
        # Stack filled in by the first DFSLoop call on tanspose of G to be used as input order on second DFSLoop call
        self.secondDFSStack = Stack()
   
    def dfs(self, i, leader, isFirstDFSLoopCall=True):
        """DFS from start DFSNode i triggered by a dfsLoop since DFSNode leader"""
        i.setExplored(True)
        self.sccs[leader].append(i)
        for j in i.getConnections():
            if not j.isExplored():
                self.dfs(j, leader)
        self.finishingTime += 1
        i.setFinish(self.finishingTime)
        if isFirstDFSLoopCall:
            self.secondDFSStack.push(i.getId())
        
    def dfsLoop(self, G, isFirstDFSLoopCall=True):
        """DFSLoop on DFSGraph G according to the vertices order in stack S"""
        self.sccs = {}
        S = None
        if isFirstDFSLoopCall:
            S = Stack()
            for i in range(1,len(G.getVertices())+1):
                node = G.getVertex(i)
                if node:
                    S.push(i)
                    node.setExplored(False)  
        else:
            S = self.secondDFSStack
            for i in G:
                i.setExplored(False)
        self.finishingTime = 0
        leader = None
        while not S.isEmpty():
            i = G.getVertex(S.pop())
            if not i.isExplored():
                leader = i
                self.sccs[leader] = []
                self.dfs(i, leader, isFirstDFSLoopCall)
        return self.sccs

    def kosarajuAlgo(self, G, Grev):
        """two DFS calls for computing SCCs according to Kosaraju's algorithm. Returns a dictionary of SCCs with leaders as keys"""
        print("First call of DFSLoop")
        for i in Grev:
                i.setExplored(False)
        self.dfsLoop(Grev, True)
        for i in Grev:
                i.setExplored(False)
        print("Second call of DFSLoop")        
        return self.dfsLoop(G, False)
        
        

        
##################
# Main() to test #
##################
def main():
    g = DFSGraph()
    grev = DFSGraph()
    try:
        f = open("SCC.txt", mode='r')
        while 1:
            line = f.readline()
            if line == '':
                break
            line.strip()
            keys= line.split()
            u = int(keys[0])
            v = int(keys[-1])
            g.addEdge(u,v)
            grev.addEdge(v,u)
        f.close()
    except:
        print("ERROR: File ", fileName, "does not exist here ", os.getcwd ())
        
    sccAlgo = KosarajuAlgo()
    res = sccAlgo.kosarajuAlgo(g, grev)
    sccSizes = []
    for leader, scc in res.items():
        sccSizes.append(len(scc))
    sccSizes.sort(reverse=True)
    print(sccSizes[:5])

if __name__ == '__main__':
    # In summary, sys.setrecursionlimit is just a limit enforced by the interpreter itself.
    # threading.stack_size lets you manipulate the actual limit imposed by the OS. If you hit the latter limit first, Python will just crash completely.
    threading.stack_size(67108864) # 64MB stack
    # to avoid RuntimeError: maximum recursion depth exceeded because by default 1000 is the limit returnt by sys.getrecursionlimit()
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target



    


    
