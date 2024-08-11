class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         hash_table = {}
         for i in range(len(nums)):
            diff = target - (nums[i])
            if diff in hash_table:
                return (i,hash_table[diff])
            else:
                hash_table[nums[i]] = i

            