class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = []
        duplicates = []

        i = 0

        while i < len(nums):
            print('index', i)
            print(nums[i])
            if nums[i] not in uniques:
                uniques.append(nums[i])
                i += 1
            else:
                duplicates.append(nums.pop(i))
        
        return len(nums)