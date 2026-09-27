class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictio = {}

        for i, val in enumerate(s):
            # print(f"i: {i}")
            for j in range(i, i+1):
                # print(j)
                # print(dictio)

                if val in dictio:
                    if dictio[val] != t[j]:
                        return False
                
                else:
                    if t[j] in dictio.values():
                        return False
                    dictio[val] = t[j]

                # if val in dictio and dictio[val] != t[j]:
                #     return False
                # elif t[j] in dictio.values() and dictio[val] != t[j]:
                #     return False
                # else:
                #     dictio[val] = t[j]
        
        # print(dictio)
        return True
                