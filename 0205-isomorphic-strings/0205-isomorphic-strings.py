class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictio = {}

        for i, val in enumerate(s):
            for j in range(i, i+1):
                # Approach 1
                # if val in dictio:
                #     if dictio[val] != t[j]:
                #         return False
                
                # else:
                #     if t[j] in dictio.values():
                #         return False

                #     dictio[val] = t[j]

                # Approach 2
                if val in dictio and dictio[val] != t[j]:
                    return False
                elif val not in dictio and t[j] in dictio.values():
                    return False
                else:
                    dictio[val] = t[j]
        return True
                