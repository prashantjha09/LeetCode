from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_dict = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_dict[secret[i]] += 1
        for i in range(len(guess)):
            if guess[i] != secret[i] and secret_dict[guess[i]] > 0:
                cows += 1
                secret_dict[guess[i]] -= 1
        return f"{bulls}A{cows}B"
