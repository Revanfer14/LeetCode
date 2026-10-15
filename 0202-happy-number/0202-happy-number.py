class Solution:
    def isHappy(self, n: int) -> bool:
        nSet = set()

        while n != 1:
            nStr = str(n)

            n = sum(int(x)**2 for x in nStr)
            
            if n in nSet:
                return False

            nSet.add(n)

            
                
        return True