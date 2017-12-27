class node(object):
    from bson.objectid import ObjectId 
    def __init__(self,neighbors = [], _id = ObjectId()):
        self._id = _id 
        self.neighbors = neighbors

    def insertNeighbor(self, _neighbor):
        self.neighbors.append(_neighbor)
    
    def __str__(self):
        string  = str(self._id)
        for neighbor in self.neighbors:
            string += '\n|_' + str(neighbor)
        return string
    
    def insertNeighbors(self, _neighbors):
        self.neighbors += _neighbors
