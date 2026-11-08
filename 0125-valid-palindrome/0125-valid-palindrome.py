import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        r = len(clean_s) - 1
        for i in clean_s:
            if i == r:
                return True
                
            if i == clean_s[r]:
                r -= 1
            else:
                return False

        return True