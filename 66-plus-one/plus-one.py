class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[:] = [str(x) for x in digits]

        digits = list(str(int(''.join(digits))+1))

        digits[:] = [int(x) for x in digits]
        
        return digits