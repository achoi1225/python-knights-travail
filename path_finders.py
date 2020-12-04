from tree import Node

class KnightPathFinder:
    def __init__(self, root):
        self._root=Node(root)
        self._considered_positions={root,}

    def get_valid_moves(self, pos):
        moves=[]
        moves.append((pos[0]+2, pos[1]+1),)
        moves.append((pos[0]+2, pos[1]-1),)
        moves.append((pos[0]+1, pos[1]+2),)
        moves.append((pos[0]+1, pos[1]-2),)
        moves.append((pos[0]-2, pos[1]+1),)
        moves.append((pos[0]-2, pos[1]-1),)
        moves.append((pos[0]-1, pos[1]+2),)
        moves.append((pos[0]-1, pos[1]-2),)
        return moves

    def new_move_positions(self, pos):
        moves = self.get_valid_moves(pos)
        validMoves = [coord for coord in moves if coord[0] >= 0 and coord[0] <= 7 and coord[1] >= 0 and coord[1] <= 7]
        filtered_moves = set(validMoves) - self._considered_positions
        self._considered_positions = self._considered_positions | set(validMoves)
        return filtered_moves

    # def build_move_tree(self):
    #     queue = [self._root]
    
    #     while queue:
    #         current_root_node = queue.pop(0)
    #         print(f"current node! {current_root_node}")

    #         new_moves = self.new_move_positions(current_root_node.value)
    #         for move in new_moves:
    #             print(f"move {move}")
    #             child_node=Node(move)
    #             current_root_node.add_child(child_node)
    #             queue.append(child_node)

    def build_move_tree(self):
        new_moves=list(self.new_move_positions(self._root.value))
        for move in new_moves:
            child_node=Node(move)
            self._root.add_child(child_node)
            
        children = [child for child in self._root.children]

        while children:
            current_root_node = children.pop(0)
            print(f"current node! {current_root_node}")

            new_moves = self.new_move_positions(current_root_node.value)
            print(f"new moves!! {new_moves}")

            for move in new_moves:
                print(f"move {move}")
                child_node=Node(move)
                current_root_node.add_child(child_node)
                children.append(child_node)
        # return

test = KnightPathFinder((0,0))
test.build_move_tree()
node_list = [test._root,]
print(f"root!!! {test._root.children}")
while node_list:
    current_node = node_list.pop(0)
    print(f"current node!! {current_node.value}")
    for child in current_node.children:
        node_list.append(child)
