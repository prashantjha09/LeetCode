class Solution:
    def __init__(self):
        self.coin_min = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
            if amount in coins:
                return 1
            if amount == 0:
                return 0
            if amount in self.coin_min:
                return self.coin_min[amount]
            tmp_coin = float("inf")
            for i in coins:
                if amount - i >= 0:
                    mc = self.coinChange(coins, amount - i)
                    if mc != -1:
                        tmp_coin = min(mc, tmp_coin)
            if tmp_coin == float("inf"):
                self.coin_min[amount] = -1
            else:
                self.coin_min[amount] = tmp_coin + 1
            return self.coin_min[amount]



            