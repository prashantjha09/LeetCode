class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Define m and n

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Initiate Metrics
        metrics = [[0] * n for _ in range(m)]


        # Starting point is blocked
        if obstacleGrid[0][0] == 1:
            return 0

        metrics[0][0] = 1

        #Create Base Case
        # First row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                print("into if")
                metrics[0][j] = 0
            else:
                metrics[0][j] = metrics[0][j-1]

        # First column
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                print("into ifed")
                metrics[i][0] = 0
            else:
                metrics[i][0] = metrics[i-1][0]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    metrics[i][j] = 0
                else:
                    metrics[i][j] = metrics[i-1][j] + metrics[i][j-1]

        return metrics[-1][-1]
