class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        nodes = defaultdict(list)

        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])
        
        connected_components = 0
        for i in range(n):
            if i in visited:
                continue
            connected_components += 1
            queue = deque([i])
            while queue:
                node = nodes[queue.popleft()]
                for sibling in node:
                    if sibling in visited:
                        continue
                    visited.add(sibling)
                    queue.append(sibling)
        
        return connected_components