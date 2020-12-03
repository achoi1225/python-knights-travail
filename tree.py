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

    
