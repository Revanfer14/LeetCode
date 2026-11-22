class Solution:
    def checkString(self, s: str) -> bool:
        curr = 'a'

        for x in s:
            if x == 'b':
                curr = 'b'
                continue
                
            if x != curr:
                return False

        return True

            
            