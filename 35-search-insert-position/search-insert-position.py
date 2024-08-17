class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] != target and target < nums[i] and i == 0:
                return 0
            elif nums[i] != target and i == len(nums)-1:
                return i+1
            elif nums[i] != target and target < nums[i+1]:
                return i+1
        
        # left = 0
        # right = len(nums)-1
        # i = 0
        
        # while left <= right:
        #     i = (left+right)//2
        #     if nums[i] == target:
        #         return i
        #     elif nums[i] < target:
        #         left = i+1
        #     else:
        #         right = i-1
        # return left

        
