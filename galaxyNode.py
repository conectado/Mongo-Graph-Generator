from node import node
class galaxyNode(node):
    
    def __init__(self, name = "", neighbors=None, _id=None, **kwargs):
        if _id is None and neighbors is None:
            node.__init__(self)
        elif _id is None:
            node.__init__(self, neighbors)
        else:
            node.__init__(self, neighbors, _id)

        self.name = name
        self.properties = kwargs or []
    
    def changeName(self, newName):
        self.name = newName
