class Solution:
    def __init__(self):
        self.min_cost_for_stairs = {}
    def min_cost(self, cost, stair):
        if stair == 0 or stair==1:
            return 0
        if stair in self.min_cost_for_stairs:
            return self.min_cost_for_stairs[stair]

        previous_step = self.min_cost(cost, stair-1) +  cost[stair-1]
        second_previous_step = self.min_cost(cost, stair-2) + cost[stair-2]

        self.min_cost_for_stairs[stair] = min(previous_step, second_previous_step)
        return self.min_cost_for_stairs[stair]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.min_cost(cost, stair=len(cost))
        


        