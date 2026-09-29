class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip() # Remove whitespaces
        b = a.split() # Turn text to array

        lengthB = len(b)

        return len(b[lengthB-1])