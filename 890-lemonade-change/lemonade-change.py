class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashier = []
        
        for bill in bills:
            if bill == 5:
                cashier.append(bill)
            elif bill == 10:
                if 5 in cashier:
                    cashier.remove(5)
                    cashier.append(10)
                else:
                    return False
            else:
                if 5 in cashier and 10 in cashier:
                    cashier.remove(5)
                    cashier.remove(10)
                elif 10 not in cashier and cashier.count(5)>=3:
                    cashier.remove(5)
                    cashier.remove(5)
                    cashier.remove(5)
                else:
                    return False
                
        return True


