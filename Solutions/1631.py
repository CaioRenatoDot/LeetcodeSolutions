import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        minHeap = [(0, 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while minHeap:
            effort, x, y = heapq.heappop(minHeap)

            if x == m - 1 and y == n - 1:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    newEffort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    if newEffort < dist[nx][ny]:
                        dist[nx][ny] = newEffort
                        heapq.heappush(minHeap, (newEffort, nx, ny))