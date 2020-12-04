class Node:
    def __init__(self, value):
        self._value=value
        self._parent=None
        self._children=[]

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent==node:
            return
        if self._parent:
            self._parent.remove_child(self)
        self._parent = node
        if self._parent != None:
            self._parent.add_child(self)

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent=self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    def depth_search(self, value):
        if self._value == value:
            return self
        if self._children:
            for child in self._children:
                result = child.depth_search(value)
                if result:
                    return result

    def breadth_search(self, value):
        if self._value == value:
            return self
        if self._children:
            nodes = self._children
            while len(nodes):
                if nodes[0].value == value:
                    return nodes[0]
                else:
                    if nodes[0].children:
                        for child in nodes[0].children:
                            nodes.append(child)
                    nodes.pop(0)

                            

# child1 = Node('child1')
# child2 = Node('child2')
# child3 = Node('child3')
# parent = Node('parent')

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# child1.add_child(a)
# child1.add_child(b)
# child2.add_child(c)
# child2.add_child(d)
# child3.add_child(e)
# child3.add_child(f)

# child2.add_child(child3)

# parent.add_child(child1)
# parent.add_child(child2)

# print(f"RESULT!! {parent.breadth_search('j')}")