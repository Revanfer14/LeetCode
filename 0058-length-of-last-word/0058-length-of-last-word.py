class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip()
        b = a.split()

        lengthB = len(b)

        return len(b[lengthB-1])