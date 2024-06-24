class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefHash = {0:1}
        count = 0

        if len(nums) == 0:
            return 0 # count is 0 if list is empty

        for num in nums:
            currSum += num

            # x = currSum - k
            # determine whether the value x is present in Hashtable
            # if present then that means there is a subarray of value x which can be subtracted from current array to create another subarray with a summed value of k
            # since you can create a value of k then that means 
            if (currSum - k) in prefHash: 
                count += prefHash[currSum-k] 
            
            if currSum in prefHash:
                prefHash[currSum] += 1
            else:
                prefHash[currSum] = 1

        return count

            
            