class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashier = []

        for bill in bills:
            if bill == 5:
                cashier.append(bill)
            elif bill == 10:
                try:
                    cashier.remove(5)
                    cashier.append(bill)
                except:
                    return False
            else:
                try:
                    cashier.remove(10)
                    cashier.remove(5)
                except:
                    try:
                        cashier.remove(5)
                        cashier.remove(5)
                        cashier.remove(5)
                    except:
                        return False
        return True
        

