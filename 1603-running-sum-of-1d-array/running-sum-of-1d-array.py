class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        sum_nums = 0

        for num in nums:
            sum_nums += num
            running.append(sum_nums)

        return running