class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1] * n
        unions = 0

        """
        n = 5
        parent = [0, 1, 2, 3, 4]
        rank   = [1, 1, 1, 1, 1]

        parent = [0, 0, 2, 3, 4]
        rank   = [1, 1, 1, 1, 1]
        """

        def find_parent(node: int) -> int:
            result = node
            while result != parent[result]:
                result = parent[result]
            return result

        def union(n1, n2) -> int:
            p1 = find_parent(n1)
            p2 = find_parent(n2)

            if p1 == p2:
                return 0

            if rank[p1] >= rank[p2]:
                rank[p1] += 1
                parent[p2] = p1
            else:
                rank[p2] += 1
                parent[p1] = p2
            return 1


        for u,v in edges:
            unions += union(u, v)

        return n - unions