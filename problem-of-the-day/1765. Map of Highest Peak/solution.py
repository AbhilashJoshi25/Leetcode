'''
1765. Map of Highest Peak

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
'''
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #get dimensions row and col
        rows = len(isWater)
        cols = len(isWater[0])

        queue = deque() # (r, c)
        ans = [[-1] * cols for index in range(rows)]

        #enqueue all the water cells
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    ans[r][c] = 0
        #BFS
        while queue:
            r, c = queue.popleft()
            h = ans[r][c]
            #make a matrix of adjacent neighbors
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or ans[nr][nc] != -1):
                    continue
                queue.append((nr, nc))
                ans[nr][nc] = h + 1
        
        return ans
