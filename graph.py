from node import node
from queue import Queue
from math import log
from random import random as rn
import pymongo
from pymongo import MongoClient
#TODO handle exceptions
class graph(object):
    def __init__(self, nodes=None):
        if nodes == None:
            nodes = []
        self.nodes = nodes

    def generate(self, n, p=None, safe = True):
        self.nodes = [] #IT RESETS ALL NODES!
        if p == None:
            p = 2*log(n)/n #If n is large enough it's probablly connected
        self.createNodes(n) 
        #TODO use itertools for cleaner code
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    if rn() <= p:
                        createEdge(node1,node2)
        if safe: #When N is small it's extremly recommended to be safe if you want the graph to be connected
            while not self.isConnected():
                self.generate(n, p, False)
        

    def createNode(self, _id = None, neighbors = None):
        self.nodes.append(node(_id, neighbors))

    def createNodes(self, n):
        for i in range(n):
            self.createNode()
    
    #This method utilize BFS, implementing a DFS could be a good idea to compare
    #Could be faster if a self.numberOfNodes is added to the class
    def isConnected(self):
        q = Queue()
        visited = []
        counted = 0 #Needed to improve computing time, could have used len(visited)
        q.put(self.nodes[0])
        visited.append(self.nodes[0])
        while not q.empty():
            visiting_node = q.get()
            counted+=1
            for n in visiting_node.neighbors:
                if n not in visited:
                    q.put(n)
                    visited.append(n)
        if counted == len(self.nodes):
            conected = True
        else:
            conected = False
        return conected
    
    def graphToMongo(self, conection, db, collection):
        mongoGraph = MongoClient(conection)[db][collection]
        mongoGraph.insert_many([x.toDict() for x in self.nodes])
        





def createEdge(node1, node2):
    node1.insertNeighbor(node2)
    node2.insertNeighbor(node1)
