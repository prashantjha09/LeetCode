class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        metrics = [[0]*n for _ in range(m)]
        metrics[0][0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j!=0:
                    metrics[0][j] = metrics[0][j-1] + grid[0][j]
                if j == 0  and i!=0:
                    metrics[i][0] = metrics[i-1][0] + grid[i][0]


        for i in range(1,m):
            for j in range(1,n):
                metrics[i][j]= min(metrics[i-1][j], metrics[i][j-1])+grid[i][j]


        return metrics[-1][-1]        