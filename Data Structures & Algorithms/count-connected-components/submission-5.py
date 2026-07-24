class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_root_parent(node: int) -> int:
            #given a node, find root of tree connecting it and return it
            root_parent = node
            while root_parent != parent[root_parent]:
                parent[root_parent] = parent[parent[root_parent]]
                root_parent = parent[root_parent]
            return root_parent

        def union(n1: int, n2: int) -> int:
            #given two nodes, connect them based on rank of their root parents. return 0 or 1 signifying if union was successful
            p1 = find_root_parent(n1)
            p2 = find_root_parent(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] >= rank[p2]:
                rank[p1] += 1
                parent[p2] = p1
            else:
                rank[p2] += 1
                parent[p1] = p2
            return 1

        
        unions = 0
        for u,v in edges:
            unions += union(u, v)

    
        return n - unions

