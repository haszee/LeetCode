class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        
        for customer in accounts:
            result.append(sum(customer))
            
        return max(result)