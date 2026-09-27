class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magz = Counter(magazine)

        for rans in ransomNote:
            print(rans)
            if rans not in magz or magz[rans] == 0:
                return False

            magz[rans] -= 1

        return True