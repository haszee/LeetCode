class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            while num%2 == 0:
                num /= 2
                count +=1
            num -= 1
            count += 1
        
        return count
        