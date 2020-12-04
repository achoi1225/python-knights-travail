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
        # print(f"filtered {filtered_moves}")
        # print(f"considered {self._considered_positions}")

        return filtered_moves

test = KnightPathFinder((0,0))
print(test.new_move_positions((0,0)))

a = {1,2,3}
b= {1,2,3,4}

print(b-a)