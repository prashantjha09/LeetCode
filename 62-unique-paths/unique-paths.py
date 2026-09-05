class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        metrics = [[-1] * m for _ in range(n)]
        for row in range(len(metrics)):
            for column in range(len(metrics[row])):
                if row == 0:
                    metrics[row][column] = 1
                if column == 0 :
                    metrics[row][column] = 1

        for row in range(len(metrics)):
            for column in range(len(metrics[row])):
                if row !=0 and column !=0:
                    metrics[row][column] = metrics[row-1][column] + metrics[row][column-1]
        return metrics[-1][-1]        