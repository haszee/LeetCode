class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] != target and target < nums[i] and i == 0:
                return 0
            elif nums[i] != target and i == len(nums)-1:
                return i+1
            elif nums[i] != target and target < nums[i+1]:
                return i+1

        
