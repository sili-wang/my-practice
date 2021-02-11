class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def count_fresh():
            fresh_oranges = [0]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        fresh_oranges[0] += 1
            return fresh_oranges

        def bfs(q, f):
            visited = set()
            mins = -1
            while q:
                temp_q = deque()
                while q:
                    i, j = q.popleft()
                    for di, dj in directions:
                        ni, nj = di + i, dj + j
                        if ni < 0 or nj < 0 or ni >= m or nj >= n:
                            continue
                        if (ni, nj) in visited:
                            continue

                        if grid[ni][nj] != 1:
                            continue

                        f[0] -= 1
                        temp_q.append((ni, nj))
                        visited.add((ni, nj))
                q = temp_q
                mins += 1
            return mins

        # add intial rotten oranges to queue
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        fresh_oranges = count_fresh()

        if fresh_oranges[0] == 0:
            return 0

        mins = bfs(q, fresh_oranges)

        return -1 if fresh_oranges[0] > 0 else mins