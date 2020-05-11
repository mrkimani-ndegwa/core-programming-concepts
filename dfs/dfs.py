class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def dFS(self, array):
        array.append(self.name)
        for c in self.children:
            c.dFS(array)
        return array

    def getChildren(self):
        return self.children
    

n = Node("Parent")
n.addChild("Child")
n.addChild("Child1")
n.addChild("Child2")
# messing arround