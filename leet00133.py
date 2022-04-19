"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        node_dict = {}
        node_que = deque([node])
        
        ret_val = Node(node.val)
        node_dict[node] = ret_val
        
        while node_que:
            cur = node_que.pop()
            new_node = node_dict[cur]
            for neighbour in cur.neighbors:
                if neighbour not in node_dict:
                    node_dict[neighbour] = Node(neighbour.val)
                    node_que.append(neighbour)  
                new_node.neighbors.append(node_dict[neighbour])
                
        return ret_val
            
