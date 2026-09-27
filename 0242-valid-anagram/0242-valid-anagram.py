class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = dict(Counter(s))
        y = dict(Counter(t))

        if x != y:
            return False
        else:
            return True