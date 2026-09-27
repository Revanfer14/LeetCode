class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictio = {}

        a = s.split()

        if len(pattern) != len(a):
            return False

        for i, val in enumerate(pattern):
            for j in range(i, i+1):

                if val in dictio and a[j] != dictio[val]:
                    return False
                elif val not in dictio and a[j] in dictio.values():
                    return False

                dictio[val] = a[j]
        
        return True