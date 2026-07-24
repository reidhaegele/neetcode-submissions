class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def valid(row: int, col: int) -> bool:
            if row < 0 or row >= len(grid):
                return False
            if col < 0 or col >= len(grid[0]):
                return False
            return True

        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] != 0:
                    continue
                seen = set()
                frontier = deque([(0, (r,c))])
                while frontier:
                    distance, coordinates = frontier.popleft()
                    row, col = coordinates
                    if (row, col) in seen:
                        continue
                    seen.add((row, col))
                    grid[row][col] = min(grid[row][col], distance)

                    for x,y in DIRECTIONS:
                        if not valid(row+y, col+x) or grid[row+y][col+x] <= 0:
                            continue
                        frontier.append((distance+1, (row+y, col+x)))
        return            