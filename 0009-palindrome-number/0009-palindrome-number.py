class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        r = len(str_x) - 1

        for l in str_x:
            if l == r:
                return True

            if l == str_x[r]:
                r -= 1
            else:
                return False

        return True
            