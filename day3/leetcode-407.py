import heapq
from collections import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])
        to_drain = []
        for i in range(rows):
            heapq.heappush(to_drain, (heightMap[i][0], [i, 0]))
            heapq.heappush(to_drain, (heightMap[i][cols-1], [i, cols-1]))
        for j in range(1, cols-1):
            heapq.heappush(to_drain, (heightMap[0][j], [0, j]))
            heapq.heappush(to_drain, (heightMap[rows-1][j], [rows-1, j]))

        rain = 0
        visited = set()
        while to_drain:
            drain_height, [i, j] = heapq.heappop(to_drain)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            rain += max(0, drain_height - heightMap[i][j])
            heightMap[i][j] = max(drain_height, heightMap[i][j])
            def check_push(check_height, m, n):
                if m < 0 or n < 0 or m >= rows or n >= cols:
                    return
                if (m, n) in visited:
                    return
                heapq.heappush(to_drain, (check_height, [m, n]))
            check_push(heightMap[i][j], i-1, j)
            check_push(heightMap[i][j], i+1, j)
            check_push(heightMap[i][j], i, j-1)
            check_push(heightMap[i][j], i, j+1)
        return rain