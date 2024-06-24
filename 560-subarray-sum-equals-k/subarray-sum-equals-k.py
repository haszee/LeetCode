class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefHash = {0:1}
        count = 0

        if len(nums) == 0:
            return 0

        for num in nums:
            currSum += num

            if (currSum - k) in prefHash:
                count += prefHash[currSum-k]
            
            if currSum in prefHash:
                prefHash[currSum] += 1
            else:
                prefHash[currSum] = 1

        return count

            
            