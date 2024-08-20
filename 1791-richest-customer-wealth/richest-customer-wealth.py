class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        
        for customer in accounts:
            money = 0
            for bank in customer:
                money += bank
            result.append(money)
        return max(result)