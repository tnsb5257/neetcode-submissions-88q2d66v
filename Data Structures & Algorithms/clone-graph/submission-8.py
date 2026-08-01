"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or not node.neighbors:
            if node:
                new_node = Node(node.val)
            else:
                new_node = None
            return new_node
        q = collections.deque()
        created = {}
        head = Node(node.val)
        created[node.val]=head
        q.append((node,head))
        while q:
            orig_node,new_node = q.popleft()
            for neighbour in orig_node.neighbors:
                if neighbour.val not in created:
                    new_neigh = Node(neighbour.val)
                    created[neighbour.val] = new_neigh
                    new_node.neighbors.append(new_neigh)
                    q.append((neighbour,new_neigh))
                else:
                    existing_neighbour_node = created.get(neighbour.val)
                    new_node.neighbors.append(existing_neighbour_node)
        return head


        