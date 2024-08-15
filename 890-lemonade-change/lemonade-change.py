class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                else:
                    fives -= 1
                    tens += 1
            else:
                if tens >= 1 and fives >=1:
                    fives -= 1
                    tens -= 1
                elif tens == 0 and fives >=3:
                    fives -= 3
                else:
                    return False
        return True


